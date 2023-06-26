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
from rest_framework.routers import DefaultRouter
import src.views as views
from src.swagger.views import custom_get_swagger_view



router = DefaultRouter()
router.register(r'location', views.LocationViewSet)
router.register(r'menu', views.MenuViewSet)
router.register(r'item', views.MenuItemViewSet)
router.register(r'schedule', views.ScheduleViewSet)


schema_view = custom_get_swagger_view(title='Open Restaurant API')

urlpatterns = [
    path('health/', views.health_check, name='health_check'),
    path('api/', include(router.urls)),
    re_path(r'^swagger/$', schema_view)
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
