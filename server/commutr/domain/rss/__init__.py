import time
from datetime import datetime

import feedparser

from commutr.celery import app
from commutr.db.news_article_model import NewsArticle
from commutr.db.news_source_keys import NewsSourceKeys
from commutr.db.news_source_model import NewsSource
from commutr.domain.pdf import download_article_content_pdf
from commutr.db.news_topic_model import NewsTopic
from commutr.domain.rss.util import get_rss_entry_data

from django.db.utils import IntegrityError


@app.task
def run_rss_workers():
    """
    A Celery beat task which will run every 20 minutes (setup in server.tasks) which will deploy
    jobs to fetch RSS feeds for each news source in the database
    """
    all_sources = NewsSource.objects.all()

    for source in all_sources:
        get_rss_articles(source)


@app.task
def get_rss_articles(news_source: NewsSource):
    """
    A Celery task for, given a news source. scraping the latest articles from the source's RSS feeds.
    These new articles are then added into the database.

    Args:
        news_source: a NewsSource instance to scrape articles from
    """

    # Parse the RSS data from the source's feed
    rss_feed = feedparser.parse(news_source.rss_url)

    latest_article = news_source.latest_article

    source_keys = NewsSourceKeys(**news_source.keys)

    for entry in rss_feed.entries:
        # Get the date of the published article
        published_time: time.struct_time = get_rss_entry_data(source_keys.published_key, entry)
        published_datetime = datetime.fromtimestamp(time.mktime(published_time)).replace(tzinfo=None)

        # If article was published before last fetch then we must have already scraped it
        if published_datetime <= latest_article.replace(tzinfo=None):
            continue

        topics = []

        try:
            # Get the topics from the RSS feed if they exist
            topics_from_rss = get_rss_entry_data(source_keys.topics_key, entry)

            topics = list(set(topics_from_rss))

            topics = [{"topic": t} for t in topics]
        except KeyError:
            # Happens when we cannot find the topics in the RSS feed
            pass

        # Create the new article with the data we fetched from the RSS feed, based on the news source's
        # specific field keys from the database
        article = NewsArticle.objects.create(
            source=news_source,
            headline=get_rss_entry_data(source_keys.headline_key, entry),
            subtitle=get_rss_entry_data(source_keys.subtitle_key, entry),
            url=get_rss_entry_data(source_keys.url_key, entry),
            image=get_rss_entry_data(source_keys.image_key, entry),
            published=published_datetime,
            topics=topics
        )

        article.save()
        latest_article = max(latest_article, article.published)

        # Fetch the article content through an async celery task
        download_article_content_pdf(article)

    news_source.latest_article = latest_article
    news_source.save()

    print("----------------------------------------------------")
