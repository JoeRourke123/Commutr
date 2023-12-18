"""
The Django models definition file.

When creating a new database model, you must import it into this file for it to be detected by
Django when making database migrations.
"""

from commutr.db.news_source_model import NewsSource
from commutr.db.news_source_topic_model import NewsSourceTopic
from commutr.db.news_article_model import NewsArticle
from commutr.db.news_article_topic_model import NewsArticleTopic
from commutr.db.news_article_content_model import NewsArticleContent