"""
URL configuration for server project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from src.swagger.views import custom_get_swagger_view
import src.views as views


# Model Views
router = DefaultRouter()
router.register(r"location", views.LocationViewSet)
router.register(r"menu", views.MenuViewSet)
router.register(r"item", views.MenuItemViewSet)
router.register(r"schedule", views.ScheduleViewSet)

# Swagger Documentation View
schema_view = custom_get_swagger_view(title="Open Restaurant API")


# URL Patterns
urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html"), name="index"),
    path("health/", views.health_check, name="health_check"),
    re_path(r"^swagger/$", schema_view, name="swagger"),
    path("register/", views.RegisterAPIView.as_view()),
    # get authentication
    path("auth/", include("dj_rest_auth.urls")),
    path("api/", include(router.urls)),
]

# In Local, serve static files locally rather than through nginx
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
