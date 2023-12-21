from django.core.management.base import BaseCommand

from commutr.domain.util.reload_sources_from_notion import reload_news_sources_from_notion


class Command(BaseCommand):
    help = "Force reload news sources from Notion into database"

    def handle(self, *args, **options):
        print("Pulling news sources from Notion")

        reload_news_sources_from_notion().apply()

        print("Successfully pulled news sources")
