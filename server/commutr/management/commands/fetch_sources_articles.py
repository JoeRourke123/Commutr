from django.core.management.base import BaseCommand

from commutr.db.news_article_model import NewsArticle
from commutr.db.news_source_model import NewsSource
from commutr.domain.pdf import download_article_content_pdf
from commutr.domain.rss import get_rss_articles


class Command(BaseCommand):
    help = "For a given news source, it will fetch their latest article PDFs"

    def handle(self, *args, **options):
        source_name = input("News Source Name > ")

        try:
            articles_to_fetch = int(input("Number of articles (leave blank to fetch all) > "))
        except ValueError:
            articles_to_fetch = None

        fetch_new_articles = input("Fetch new articles? (y/n) > ")

        news_source = NewsSource.objects.get(name=source_name)

        if fetch_new_articles == 'y':
            get_rss_articles(news_source)

        articles = NewsArticle.objects.filter()

        if articles_to_fetch is not None:
            articles = articles[:articles_to_fetch]

        for article in articles:
            download_article_content_pdf(article)
