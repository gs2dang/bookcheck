from django.contrib import admin

from .models import SearchList


@admin.register(SearchList)
class SearchListAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'author', 'publisher', 'date', 'updated']
    list_per_page = 20
