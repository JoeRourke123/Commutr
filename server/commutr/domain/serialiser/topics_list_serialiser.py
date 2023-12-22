from commutr.db.news_article_model import NewsArticle
from commutr.db.news_topic_model import NewsTopic
from rest_framework import serializers


class NewsTopicsListSerialiser(serializers.Field):
    many = True

    def get_attribute(self, instance: NewsArticle):
        # We pass the object instance onto `to_representation`,
        # not just the field attribute.
        return instance

    def to_representation(self, value: NewsArticle):
        """
        Serialize the value's class name.
        """
        return map(lambda t: t["topic"], value.topics)