import uuid
from datetime import datetime
from uuid import UUID

from django.core import validators
from djongo import models

from commutr.db.news_source_keys import NewsSourceKeys
from commutr.db.news_topic_model import NewsTopic
from commutr.domain.util.constants import DEFAULT_KEYS


class NewsSource(models.Model):
    """
    Represents a single news source/vendor
    """

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_column="source_id")  # Unique identifier used for sources internally by us

    name = models.CharField(db_column="source_name", editable=False, max_length=128)    # e.g. The Guardian

    rss_url = models.URLField(db_column="source_rss_feed_url", editable=False)  # The URL of the RSS feed we scrape articles from for this source

    political_leaning = models.FloatField(validators=(
        validators.MinValueValidator(-1.0),
        validators.MaxValueValidator(1.0),
    ), db_column="source_political_leaning", editable=False)    # -1 is very left-wing, 1 is very conservative. 0 is centrism.

    latest_article = models.DateTimeField(
        db_column="source_latest_article",
        default=datetime(1970, 1, 1),
        null=True,
        editable=True
    )  # The date/time of the most recent article scraped, used to identify which articles have already been pulled

    # -- The Keys --
    # So these key fields are used to represent where to find certain data in the source's RSS response
    # for example the key `data.links[1].href` would return response['data']['links'][1]['href']
    keys = models.EmbeddedField(
        model_container=NewsSourceKeys,
        db_column="source_keys",
        default=DEFAULT_KEYS
    )

    topics = models.ArrayField(
        model_container=NewsTopic,
        db_column="source_topics",
        default=[]
    )

    class Meta:
        db_table = "news_source"  # Mongo table name
