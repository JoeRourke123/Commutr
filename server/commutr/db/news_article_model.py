import uuid

from django.db import models

from commutr.db.news_source_model import NewsSource


class NewsArticle(models.Model):
    id = models.UUIDField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False
    )

    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="articles",
        db_column="news_source_id",
        editable=False
    )

    headline = models.CharField(
        max_length=512,
        db_column="article_headline",
        editable=False
    )

    subtitle = models.CharField(
        max_length=2048,
        db_column="article_subtitle",
        null=True,
        editable=False
    )

    image = models.URLField(
        db_column="article_image_url",
        null=True,
        editable=False
    )

    published = models.DateTimeField(
        db_column="article_published",
        editable=False
    )

    url = models.URLField(
        db_column="article_url",
        editable=False
    )

    author = models.CharField(
        db_column="article_author",
        editable=False
    )

    class Meta:
        db_table = "news_article"
        ordering = ['-published']
