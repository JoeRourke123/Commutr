from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action

from commutr.domain.serialiser.digest_item_serialiser import DigestItemSerialiser


TEST_STOCKS = ["EXPE", "APPL", "TSLA"]
TEST_HOROSCOPE = datetime(year=2001, month=8, day=22)
TEST_WEATHER_COORDS = (51.590360, -0.102780, )


class DigestController(viewsets.ViewSet):
    serializer_class = DigestItemSerialiser

    @action(methods=["GET"], url_path="/")
    def get_digest(self, request):
        """
        The endpoint to fetch the users generated digest (/api/digest)

        Args:
            request: The Django request information

        Returns:
            A list of DigestItems containing articles/stocks/games/etc
        """

