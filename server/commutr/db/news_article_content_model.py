from django.db import models

from commutr.db.news_article_model import NewsArticle


class NewsArticleContent(models.Model):
    article = models.OneToOneField(
        NewsArticle,
        on_delete=models.CASCADE,
        db_column="news_article_id",
        related_name="content",
        primary_key=True,
        editable=False
    )

    content = models.BinaryField(
        db_column="news_article_content",
        editable=False
    )

    class Meta:
        db_table = "news_article_content"

