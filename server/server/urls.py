from rest_framework.routers import DefaultRouter

from commutr.controller.fallback_article_fetch_controller import FallbackArticleFetchController

router = DefaultRouter()
router.register(r'api', FallbackArticleFetchController)
urlpatterns = router.urls
