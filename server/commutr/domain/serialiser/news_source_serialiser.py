from rest_framework import serializers

from commutr.db.news_source_model import NewsSource


class NewsSourceSerialiser(serializers.ModelSerializer):
    topics = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='topic'
    )

    class Meta:
        model = NewsSource
        fields = ('id', 'name', 'political_leaning', 'topics')
