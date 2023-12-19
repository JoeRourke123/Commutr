from commutr.celery import app

from notion_client import Client

from commutr.db.news_source_model import NewsSource
from commutr.db.news_source_topic_model import NewsSourceTopic
from server import settings


@app.task
def reload_news_sources_from_notion():
    notion_client = Client(auth=settings.NOTION_API_TOKEN)

    # Get database entries from Notion
    news_source_database = notion_client.databases.query(settings.NEWS_SOURCES_BASE_ID)

    for news_source in news_source_database["results"]:
        name = news_source["properties"]["name"]["title"][0]["plain_text"]
        rss_url = news_source["properties"]["rss_url"]["rich_text"][0]["plain_text"]
        political_leaning = news_source["properties"]["political_leaning"]["number"]
        author_key = news_source["properties"]["author_key"]["rich_text"][0]["plain_text"]
        headline_key = news_source["properties"]["headline_key"]["rich_text"][0]["plain_text"]
        image_key = news_source["properties"]["image_key"]["rich_text"][0]["plain_text"]
        published_key = news_source["properties"]["published_key"]["rich_text"][0]["plain_text"]
        subtitle_key = news_source["properties"]["subtitle_key"]["rich_text"][0]["plain_text"]
        url_key = news_source["properties"]["url_key"]["rich_text"][0]["plain_text"]

        # website_url = news_source["properties"]["value"]["rich_text"][0]["plain_text"]

        news_source, created = NewsSource.objects.update_or_create(
            name=name,
            defaults={
                "rss_url": rss_url, "political_leaning": political_leaning, "author_key": author_key,
                "headline_key": headline_key, "image_key": image_key, "published_key": published_key,
                "subtitle_key": subtitle_key, "url_key": url_key
            }
        )
        news_source.save()

        topics = news_source["properties"]["topics"]["multi_select"]

        for topic in topics:
            topic, created = NewsSourceTopic.objects.get_or_create(
                news_source=news_source,
                topic=topic["name"]
            )
            topic.save()

