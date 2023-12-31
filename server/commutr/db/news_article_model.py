import uuid

from djongo import models

from commutr.db.news_source_model import NewsSource
from commutr.db.news_topic_model import NewsTopic


class NewsArticle(models.Model):
    """
    Represents a single news article
    """

    # Our randomly generated UUID for the article
    id = models.CharField(
        default=uuid.uuid4,
        primary_key=True,
        editable=False,
        max_length=36
    )

    # The publication the article comes from, represented as a relation to the NewsSource table.
    source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="articles",
        db_column="news_source_id",
        editable=False,
        max_length=128
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

    # Represents a link to an image on the article page
    image = models.URLField(
        db_column="article_image_url",
        null=True,
        editable=False
    )

    # What date and time was the article released?
    published = models.DateTimeField(
        db_column="article_published",
        editable=False
    )

    # What URL can you go to in order to reach the original article
    url = models.URLField(
        db_column="article_url",
        editable=False
    )

    author = models.CharField(
        db_column="article_author",
        editable=False,
        max_length=256
    )

    topics = models.ArrayField(
        db_column="article_topics",
        model_container=NewsTopic,
        default=[]
    )

    content = models.BinaryField(
        db_column="article_content",
        editable=False,
        null=True,
        default=None
    )

    class Meta:
        db_table = "news_article"  # Actual table name in Postgres
        ordering = ['-published']  # Orders the table by newest articles first
