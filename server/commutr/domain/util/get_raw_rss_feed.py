import feedparser


def get_raw_rss_feed(rss_url = None):
    """
    Simple helper function which given an RSS URL will just print out the first entry as an example
    Args:
        rss_url: a str URL for an RSS feed. If blank, the user will be prompted to enter one

    Returns:
        A JSON representation of one RSS feed article.
    """

    if rss_url is None:
        rss_url = input("Please enter RSS URL > ")

    parsed_rss = feedparser.parse(rss_url)

    first_entry = parsed_rss.entries[0]

    print(first_entry)


if __name__ == "__main__":
    get_raw_rss_feed()
