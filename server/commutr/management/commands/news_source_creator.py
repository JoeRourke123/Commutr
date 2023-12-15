import uuid

from django.core.management.base import BaseCommand
from django.db.models import ForeignObjectRel, ForeignObject, UUIDField

from commutr.db.news_source_model import NewsSource
from commutr.db.news_source_topic_model import NewsSourceTopic
from commutr.domain.util.get_raw_rss_feed import get_raw_rss_feed


class Command(BaseCommand):
    help = "Creates a new news source with user entered information and saves it to the database"

    def handle(self, *args, **options):
        fields = NewsSource._meta.get_fields()
        new_source_args = {}

        print("Creating a new news source... Enter the following details when prompted. \n")

        for field in fields:
            if isinstance(field, ForeignObjectRel) or isinstance(field, ForeignObject):
                continue
            elif isinstance(field, UUIDField):
                new_source_args[field.name] = uuid.uuid4()
                continue

            field_value = input(f"{field.name} > ")

            if field.name == "rss_url":
                print("------- Printing Example RSS Entry -------")
                get_raw_rss_feed(field_value)
                print("------------------------------------------")

            if field_value == "":
                if not field.null:
                    raise ValueError(f"Field '{ field.name }' cannot be blank or null.")

                new_source_args[field.name] = None
            else:
                new_source_args[field.name] = field_value

        new_source = NewsSource.objects.create(**new_source_args)

        new_source.save()

        print(f"{ new_source.name } has been created... \n")

        topic = input("Enter a topic the source covers > ")

        while topic != "":
            new_topic = NewsSourceTopic.objects.create(
                news_source=new_source,
                topic=topic
            )
            new_topic.save()

            topic = input("Enter another topic the source covers > ")