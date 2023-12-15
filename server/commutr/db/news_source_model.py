import uuid
from uuid import UUID

from django.core import validators
from django.db import models


class NewsSource(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)

    name = models.CharField(db_column="source_name")

    rss_url = models.URLField(db_column="rss_feed_url")

    political_leaning = models.FloatField(validators=(
        validators.MinValueValidator(-1.0),
        validators.MaxValueValidator(1.0),
    ))

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
        db_table = "news_source"
