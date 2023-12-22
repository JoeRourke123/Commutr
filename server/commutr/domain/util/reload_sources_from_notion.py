from commutr.celery import app

from notion_client import Client

from commutr.db.news_source_keys import NewsSourceKeys
from commutr.db.news_source_model import NewsSource

from commutr.db.news_topic_model import NewsTopic
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

        keys = ["author_key", "headline_key", "image_key", "published_key", "subtitle_key", "url_key", "topics_key"]
        key_map = {}

        for key in keys:
            try:
                key_map[key] = news_source["properties"][key]["rich_text"][0]["plain_text"]
            except IndexError or KeyError:
                key_map[key] = None

        topics = news_source["properties"]["topics"]["multi_select"]

        # website_url = news_source["properties"]["value"]["rich_text"][0]["plain_text"]

        news_source, created = NewsSource.objects.update_or_create(
            name=name,
            defaults={
                "rss_url": rss_url, "political_leaning": political_leaning, "keys": key_map,
                "topics": [{"topic": t["name"]} for t in topics]
            }
        )

        news_source.save()
