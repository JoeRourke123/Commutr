from django.db import models

from commutr.db.news_source_model import NewsSource


class NewsSourceTopic(models.Model):
    news_source = models.ForeignKey(
        NewsSource,
        on_delete=models.CASCADE,
        related_name="topics",
        db_column="news_source_id"
    )

    topic = models.CharField(
        max_length=128,
    )

    class Meta:
        unique_together = (
            ('news_source', 'topic')
        )
        db_table = "news_source_topic"
