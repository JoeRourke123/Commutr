"""
The Django URLs file.

In this file, any exposed URLs for the service must be exposed. Here we are exposing our API
endpoints defined in our Controller viewsets from `commutr/controller/`
"""
from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from commutr.controller.fallback_article_fetch_controller import FallbackArticleFetchController
from commutr.controller.social_login_controller import GoogleLogin, AppleLogin

router = DefaultRouter()
router.register(r'api/articles', FallbackArticleFetchController)

# urlpatterns is imported by Django to know which URLs the server should accept
urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/auth/', include('dj_rest_auth.urls')),
    path('api/auth/signup/', include('dj_rest_auth.registration.urls')),
    path('api/auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('api/auth/apple/', AppleLogin.as_view(), name='apple_login'),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    *router.urls,
]
