from commutr.domain.serialiser.topics_list_serialiser import NewsTopicsListSerialiser
from rest_framework import serializers

from commutr.db.news_source_model import NewsSource


class NewsSourceSerialiser(serializers.ModelSerializer):
    """
    Serialises Django NewsSource models to JSON
    """

    topics = NewsTopicsListSerialiser(
        read_only=True
    )

    class Meta:
        model = NewsSource
        # What fields are we including the serialiser? Not any internal RSS key ones as the user
        # doesn't need to know.
        fields = ('id', 'name', 'political_leaning', 'topics')
