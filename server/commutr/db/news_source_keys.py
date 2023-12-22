from djongo import models


class NewsSourceKeys(models.Model):
    url_key = models.CharField(
        max_length=128,
        editable=False,
        primary_key=True,
    )

    headline_key = models.CharField(
        max_length=128,
        editable=False
    )

    image_key = models.CharField(
        max_length=128,
        null=True,
        editable=False,
        default=None,
    )

    subtitle_key = models.CharField(
        max_length=128,
        null=True,
        editable=False,
        default=None,
    )

    author_key = models.CharField(
        max_length=128,
        null=True,
        editable=False,
        default=None,
    )

    published_key = models.CharField(
        max_length=128,
        editable=False,
    )

    topics_key = models.CharField(
        max_length=128,
        null=True,
        default=None,
        editable=False
    )

    class Meta:
        pass
