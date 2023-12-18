from rest_framework import serializers

from commutr.db.news_article_model import NewsArticle
from commutr.domain.serialiser.news_source_serialiser import NewsSourceSerialiser


class NewsArticleSerialiser(serializers.ModelSerializer):
    """
    Serialises Django NewsArticles models to JSON
    """

    # Converts topics relation to list of string topics which are related to the article
    topics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='topic'
    )

    # When serialising an article, serialise the related news source object
    source = NewsSourceSerialiser(
        many=False,
        read_only=True
    )

    class Meta:
        model = NewsArticle
        # Which fields should we include in this serialisation?
        fields = ('id', 'headline', 'subtitle', 'author', 'published', 'url', 'topics', 'image', 'source')
