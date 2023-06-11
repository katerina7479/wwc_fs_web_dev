from django.contrib import admin

# Register your models here.
from .models import Location, Menu, MenuItem, MenuSection, Schedule

admin.site.register(Location)
admin.site.register(Menu)
admin.site.register(MenuItem)
admin.site.register(MenuSection)
admin.site.register(Schedule)
