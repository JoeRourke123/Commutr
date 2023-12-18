from django.db import models

from commutr.db.news_article_model import NewsArticle


class NewsArticleTopic(models.Model):
    """
    Provides a many-to-one mapping of topics to article
    """

    # Relation to the article through a foreign key
    article = models.ForeignKey(
        NewsArticle,
        related_name="topics",      # Related name allows us to access these records from .topics on a NewsArticle instance
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
            ('article', 'topic')        # Creates a composite primary key with the two fields
        )
        db_table = "news_article_topic"     # Postgres table name
