from django.db import models


class NewsTopic(models.Model):
    """
    Provides an encapsulation of topic strings
    """
    topic = models.CharField(
        max_length=128,
        primary_key=True
    )
