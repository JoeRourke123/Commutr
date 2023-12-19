from django.core.management.base import BaseCommand

from notion.client import NotionClient
from md2notion.upload import upload


class Command(BaseCommand):
    help = "Publishes generated Markdown documentation to Notion"

    def add_arguments(self, parser):
        parser.add_argument('notion_token_v2', type=str)
        parser.add_argument('notion_docs_page_id', type=str)

    def handle(self, *args, **options):
        notion_client = NotionClient(token_v2=options["notion_token_v2"])
        docs_page = notion_client.get_block(options["notion_docs_page_id"])

        docs_page.locked = False

        with open("docs/commutr.md", "r+", encoding="utf-8") as docs_file:
            for child in docs_page.children[1:]:
                child.remove()

            previous_line = ""
            trimmed_docs_file = ""
            for line in docs_file.readlines():
                if not line.strip():
                    trimmed_docs_file += line
                    continue

                if line.startswith("# ") and previous_line.startswith("# "):
                    previous_line = line
                else:
                    if previous_line.startswith("# "):
                        trimmed_docs_file += "---- \n"

                    trimmed_docs_file += previous_line
                    previous_line = line

            docs_file.truncate(0)
            docs_file.seek(0)
            docs_file.write(trimmed_docs_file)

        with open("docs/commutr.md", "r", encoding="utf-8") as docs_file:
            upload(docs_file, docs_page)

        docs_page.locked = True
