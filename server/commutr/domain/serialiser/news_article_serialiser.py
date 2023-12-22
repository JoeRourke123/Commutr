from commutr.domain.serialiser.topics_list_serialiser import NewsTopicsListSerialiser
from rest_framework import serializers

from commutr.db.news_article_model import NewsArticle
from commutr.domain.serialiser.news_source_serialiser import NewsSourceSerialiser


class NewsArticleSerialiser(serializers.ModelSerializer):
    """
    Serialises Django NewsArticles models to JSON
    """
    # When serialising an article, serialise the related news source object
    source = NewsSourceSerialiser(
        many=False,
        read_only=True
    )

    topics = NewsTopicsListSerialiser(
        read_only=True
    )

    class Meta:
        model = NewsArticle
        # Which fields should we include in this serialisation?
        fields = ('id', 'headline', 'subtitle', 'author', 'published', 'url', 'topics', 'image', 'source')
