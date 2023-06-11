import django_filters
from .models import Menu


class MenuFilter(django_filters.FilterSet):
    class Meta:
        model = Menu
        fields = {
            'location': ['exact'],
            'active': ['exact'],
            'active_from': ['exact', 'gt', 'gte', 'lt', 'lte'],
            'active_to': ['exact', 'gt', 'gte', 'lt', 'lte'],
        }
