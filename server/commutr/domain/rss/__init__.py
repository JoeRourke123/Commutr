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
    rss_feed = feedparser.parse(news_source.rss_url)

    for entry in rss_feed.entries:
        published_date: time.struct_time = get_rss_entry_data(news_source.published_key, entry)
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
            topics = get_rss_entry_data(news_source.topics_key, entry)

            for topic in topics:
                try:
                    news_article_topic = NewsArticleTopic.objects.create(
                        article=article,
                        topic=topic
                    )

                    news_article_topic.save()
                except IntegrityError:
                    continue
        except KeyError:
            return

    print("----------------------------------------------------")
