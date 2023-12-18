from django.db import models

from commutr.db.news_article_model import NewsArticle


class NewsArticleContent(models.Model):
    """
    A table which provides a one-to-one mapping of articles to their content.
    """

    article = models.OneToOneField(
        NewsArticle,
        on_delete=models.CASCADE,
        db_column="news_article_id",
        related_name="content",
        primary_key=True,
        editable=False
    )

    # Stores raw binary representation of the article contents as a PDF file
    content = models.BinaryField(
        db_column="news_article_content",
        editable=False
    )

    class Meta:
        db_table = "news_article_content"       # The table name in Postgres

