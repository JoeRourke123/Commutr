from django.db import models

from commutr.db.news_article_model import NewsArticle


class NewsArticleTopic(models.Model):
    article = models.ForeignKey(
        NewsArticle,
        related_name="topics",
        db_column="news_article_id",
        on_delete=models.CASCADE,
        editable=False
    )

    topic = models.CharField(
        max_length=128,
        editable=False
    )

    class Meta:
        unique_together = (
            ('article', 'topic')
        )
        db_table = "news_article_topic"
