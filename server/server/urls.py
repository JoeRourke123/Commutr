"""
The Django URLs file.

In this file, any exposed URLs for the service must be exposed. Here we are exposing our API
endpoints defined in our Controller viewsets from `commutr/controller/`
"""

from rest_framework.routers import DefaultRouter

from commutr.controller.fallback_article_fetch_controller import FallbackArticleFetchController

router = DefaultRouter()
router.register(r'api', FallbackArticleFetchController)
router.register(r'api/digest', FallbackArticleFetchController)

# urlpatterns is imported by Django to know which URLs the server should accept
urlpatterns = router.urls
