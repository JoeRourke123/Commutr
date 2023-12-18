import uuid

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.http import HttpResponse

from commutr.db.news_article_model import NewsArticle
from commutr.db.news_source_model import NewsSource
from commutr.domain.article.article_service import ArticleService
from commutr.domain.serialiser.news_article_serialiser import NewsArticleSerialiser


class FallbackArticleFetchController(viewsets.ReadOnlyModelViewSet):
    """
    This is a temporary ViewSet, created for keeping a set of common and useful endpoints.
    This will be refactored into more concrete controllers upon further iterations.
    """
    article_service = ArticleService()

    # These are required by Django ViewSets
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerialiser

    @action(detail=False, methods=['get'])
    def articles(self, request):
        """
        This GET endpoints /api/articles returns the most recent 10 articles

        Args:
            request: the Django request data

        Returns:
            a serialised list of the 10 most recent articles
        """

        serialised = self.serializer_class(
            self.article_service.get_articles(limit=10),
            many=True
        )

        return Response(serialised.data)

    @action(detail=False, methods=['get'], url_path="source/(?P<pk>[\w-]+)/articles")
    def articles_by_source(self, request, pk: uuid.UUID):
        """
        This GET endpoint api/source/SOURCE_ID/articles returns the articles from a given source.

        Args:
            request: the Django request data
            pk: the primary key/UUID of a news source

        Returns:
            a serialised list of articles from the specified source
        """

        news_source = NewsSource.objects.get(id=pk)
        serialised = self.serializer_class(
            self.article_service.get_articles_by_source(news_source),
            many=True
        )

        return Response(serialised.data)

    @action(detail=False, methods=['get'], url_path="article/(?P<pk>[\w-]+)")
    def article_with_content(self, request, pk: uuid.UUID):
        """
        This GET endpoint /api/article/ARTICLE_ID returns the PDF contents of the specified article

        Args:
            request: the Django request data
            pk: the UUID of a news article

        Returns:
            a HTTP response of type application/pdf with the binary article content PDF
        """

        news_article = NewsArticle.objects.get(id=pk)
        return HttpResponse(
            self.article_service.get_article_content(news_article),

            # These headers are set to ensure the browser can interpet the PDF file
            content_type="application/pdf",
            headers={
                # Set the default file download name equal the article ID
                'Content-Disposition': f'filename={news_article.id}.pdf'
            }
        )
