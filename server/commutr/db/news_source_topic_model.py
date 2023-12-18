from django.db import models

from commutr.db.news_source_model import NewsSource


class NewsSourceTopic(models.Model):
    """
    Provides a many-to-one mapping of topics to news source
    """

    news_source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="topics",          # Related name allows us to access these records from .topics on a NewsArticle instance
        db_column="news_source_id"
    )

    topic = models.CharField(
        max_length=128,
    )

    class Meta:
        unique_together = (
            ('news_source', 'topic')             # Creates a composite primary key with the two fields
        )
        db_table = "news_source_topic"           # Postgres table name
