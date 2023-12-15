from rest_framework import serializers

from commutr.db.news_article_model import NewsArticle
from commutr.domain.serialiser.news_source_serialiser import NewsSourceSerialiser


class NewsArticleSerialiser(serializers.ModelSerializer):
    topics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='topic'
    )

    source = NewsSourceSerialiser(
        many=False,
        read_only=True
    )

    class Meta:
        model = NewsArticle
        fields = ('id', 'headline', 'subtitle', 'author', 'published', 'url', 'topics', 'image', 'source')
