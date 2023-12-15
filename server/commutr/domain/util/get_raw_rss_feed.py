import feedparser


def get_raw_rss_feed(rss_url = None):
    if rss_url is None:
        rss_url = input("Please enter RSS URL > ")

    parsed_rss = feedparser.parse(rss_url)

    first_entry = parsed_rss.entries[0]

    print(first_entry)


if __name__ == "__main__":
    get_raw_rss_feed()
