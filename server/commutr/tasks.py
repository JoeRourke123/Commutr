"""
The Celery tasks definition file.

Much like `models.py`, here we import the tasks we wish to deploy with Celery so they can be detected
by the Celery worker.
"""

from commutr.domain.rss import get_rss_articles
from commutr.domain.pdf import download_article_content_pdf
