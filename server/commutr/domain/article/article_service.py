import io
from datetime import datetime

from django.db.models import BinaryField

from commutr.db.news_article_model import NewsArticle
from commutr.db.news_source_model import NewsSource


class ArticleService(object):
    def get_articles(self, sources: [NewsSource] = None, after_date: datetime = None, limit: int = None):
        articles = NewsArticle.objects.filter(content__isnull=False)

        if sources:
            articles = articles.filter(source__in=sources)
        if after_date:
            articles = articles.filter(published__gt=after_date)
        if limit:
            articles = articles[:limit]

        return articles

    def get_articles_by_source(self, source: NewsSource, after_date: datetime = None):
        return self.get_articles(sources=[source], after_date=after_date)

    def get_articles_after_date(self, after_date: datetime):
        return self.get_articles(after_date=after_date)

    def get_article_content(self, article: NewsArticle):
        return bytes(article.content.content)
