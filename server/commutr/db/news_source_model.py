import uuid
from uuid import UUID

from django.core import validators
from django.db import models


class NewsSource(models.Model):
    """
    Represents a single news source/vendor
    """

    # Unique identifier used for sources internally by us
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    # e.g. The Guardian
    name = models.CharField(db_column="source_name")

    # The URL of the RSS feed we scrape articles from for this source
    rss_url = models.URLField(db_column="rss_feed_url")

    # -1 is very left-wing, 1 is very conservative. 0 is centrism.
    political_leaning = models.FloatField(validators=(
        validators.MinValueValidator(-1.0),
        validators.MaxValueValidator(1.0),
    ))

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
        db_table = "news_source"        # Postgres table name
