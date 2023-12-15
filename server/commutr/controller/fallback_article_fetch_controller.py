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
    article_service = ArticleService()
    queryset = NewsArticle.objects.all()
    serializer_class = NewsArticleSerialiser

    @action(detail=False, methods=['get'])
    def articles(self, request):
        serialised = self.serializer_class(
            self.article_service.get_articles(limit=10),
            many=True
        )

        return Response(serialised.data)

    @action(detail=False, methods=['get'], url_path="source/(?P<pk>[\w-]+)/articles")
    def articles_by_source(self, request, pk: uuid.UUID):
        news_source = NewsSource.objects.get(id=pk)
        serialised = self.serializer_class(
            self.article_service.get_articles_by_source(news_source),
            many=True
        )

        return Response(serialised.data)

    @action(detail=False, methods=['get'], url_path="article/(?P<pk>[\w-]+)")
    def article_with_content(self, request, pk: uuid.UUID):
        news_article = NewsArticle.objects.get(id=pk)
        return HttpResponse(
            self.article_service.get_article_content(news_article),
            content_type="application/pdf",
            headers={
                'Content-Disposition': f'filename={news_article.id}.pdf'
            }
        )
