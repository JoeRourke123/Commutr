import time
from datetime import datetime

import feedparser

from commutr.celery import app
from commutr.db.news_article_model import NewsArticle
from commutr.db.news_article_topic_model import NewsArticleTopic
from commutr.db.news_source_model import NewsSource
from commutr.domain.rss.util import get_rss_entry_data

from django.db.utils import IntegrityError

@app.task
def get_rss_articles(news_source: NewsSource):
    """
    A Celery task for, given a news source. scraping the latest articles from the source's RSS feeds.
    These new articles are then added into the database.

    Args:
        news_source: a NewsSource instance to scrape articles from

    Returns:
        N/A.
    """

    # Parse the RSS data from the source's feed
    rss_feed = feedparser.parse(news_source.rss_url)

    for entry in rss_feed.entries:
        # Get the date of the published article
        published_date: time.struct_time = get_rss_entry_data(news_source.published_key, entry)

        # Create the new article with the data we fetched from the RSS feed, based on the news source's
        # specific field keys from the database
        article = NewsArticle.objects.create(
            source=news_source,
            headline=get_rss_entry_data(news_source.headline_key, entry),
            subtitle=get_rss_entry_data(news_source.subtitle_key, entry),
            url=get_rss_entry_data(news_source.url_key, entry),
            image=get_rss_entry_data(news_source.image_key, entry),
            published=datetime.fromtimestamp(time.mktime(published_date))
        )

        article.save()

        try:
            # Get the topics from the RSS feed if they exist
            topics = get_rss_entry_data(news_source.topics_key, entry)

            for topic in topics:
                try:
                    # Create a new NewsArticleTopic for each topic belonging to the article.
                    # TODO: add a way to retrieve topics in case they are not in the RSS feed.
                    news_article_topic = NewsArticleTopic.objects.create(
                        article=article,
                        topic=topic
                    )

                    news_article_topic.save()
                except IntegrityError:
                    # Happens when topic/article combo is duplicated
                    continue
        except KeyError:
            # Happens when we cannot find the topics in the RSS feed
            return

    print("----------------------------------------------------")
