# flake8: ignore=F405
from django.contrib import admin

from .models import *


# class SettingsAdmin(admin.ModelAdmin):
# list_display = "lang"
# list_display_links = "id"
# search_fields = "name"


admin.site.register(Settings)  # noqa


class BlockedSitesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "url")
    list_display_links = ("id", "name")


admin.site.register(BlockedSites, BlockedSitesAdmin)  # noqa
