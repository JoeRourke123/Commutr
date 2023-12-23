import io
from datetime import datetime

from commutr.db.news_article_model import NewsArticle
from commutr.db.news_source_model import NewsSource


class ArticleService(object):
    """
    An encapsulated abstraction layer for fetching article records from the database
    """

    def get_articles(self, sources: [NewsSource] = None, after_date: datetime = None, limit: int = None):
        """
        Fetches articles that meet the provided criteria

        Args:
            sources: A list of NewsSource objects to fetch from. If the field is None, return from any source
            after_date: Only return articles from after this datetime, unless it is None then return records from any date
            limit: An integer limit on the number of fetched articles. Unless None, then no limits are placed

        Returns:
            A list of NewsArticle objects filtered according to the method parameters
        """

        articles = NewsArticle.objects.filter(content__isnull=False)

        if sources:
            articles = articles.filter(source__in=sources)
        if after_date:
            articles = articles.filter(published__gt=after_date)
        if limit:
            articles = articles[:limit]

        return articles

    def get_articles_by_source(self, source: NewsSource, after_date: datetime = None):
        """
        Given a specific source, find all their articles

        Args:
            source: the NewsSource to fetch
            after_date: an optional datetime filter, if present only articles after the specified datetime are included

        Returns:
            A filtered list of NewsArticle instances from the specified news source
        """

        return self.get_articles(sources=[source], after_date=after_date)

    def get_articles_after_date(self, after_date: datetime):
        """
        Returns NewsArticles only from after the specified datetime
        Args:
            after_date: A non-nullable datetime set as the lower bound for the article filter

        Returns:
            A list of NewsArticle instances which came after after_date
        """

        return self.get_articles(after_date=after_date)

    def get_article_content(self, article: NewsArticle):
        """
        For a given article, fetch its PDF content from the database

        Args:
            article: the NewsArticle metadata to fetch the content for

        Returns:
            The bytes for a PDF containing article content
        """

        return bytes(article.content)
