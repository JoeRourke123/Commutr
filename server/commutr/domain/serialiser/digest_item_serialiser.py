from rest_framework import serializers

from commutr.domain.util.digest_item_type import DigestItemType


class DigestItemSerialiser(serializers.Serializer):
    item_type = serializers.ChoiceField(
        choices=DigestItemType.get_item_types(),
        read_only=True
    )

    item_content = serializers.JSONField(
        required=True,
        read_only=True
    )
