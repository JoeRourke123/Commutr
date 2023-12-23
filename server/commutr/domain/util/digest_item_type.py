from enum import Enum


class DigestItemType(Enum):
    ARTICLE = 1
    GAME = 2
    STOCKS = 3
    HOROSCOPE = 4
    PLAYLIST = 5
    AD = 6
    WEATHER = 7

    @classmethod
    def get_item_types(cls) -> [str]:
        return [t.name for t in cls]
