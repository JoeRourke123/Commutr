import uuid
from datetime import datetime
from uuid import UUID

from django.core import validators
from django.db import models


class NewsSource(models.Model):
    """
    Represents a single news source/vendor
    """

    # Unique identifier used for sources internally by us
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, db_column="source_id")

    # e.g. The Guardian
    name = models.CharField(db_column="source_name", editable=False)

    # The URL of the RSS feed we scrape articles from for this source
    rss_url = models.URLField(db_column="source_rss_feed_url", editable=False)

    # -1 is very left-wing, 1 is very conservative. 0 is centrism.
    political_leaning = models.FloatField(validators=(
        validators.MinValueValidator(-1.0),
        validators.MaxValueValidator(1.0),
    ), db_column="source_political_leaning", editable=False)

    # The date/time of the most recent article scraped, used to identify which articles
    # have already been pulled
    latest_article = models.DateTimeField(
        db_column="source_latest_article",
        default=datetime(1970, 1, 1),
        null=True,
        editable=True
    )

    # -- The Keys --
    # So these key fields are used to represent where to find certain data in the source's RSS response
    # for example the key `data.links[1].href` would return response['data']['links'][1]['href']
    url_key = models.CharField(
        max_length=128,
        editable=False
    )

    headline_key = models.CharField(
        max_length=128,
        editable=False
    )

    image_key = models.CharField(
        max_length=128,
        null=True,
        editable=False
    )

    subtitle_key = models.CharField(
        max_length=128,
        null=True,
        editable=False
    )

    author_key = models.CharField(
        max_length=128,
        null=True,
        editable=False
    )

    published_key = models.CharField(
        max_length=128,
        editable=False
    )

    topics_key = models.CharField(
        max_length=128,
        null=True,
        editable=False
    )

    class Meta:
        db_table = "news_source"  # Postgres table name
