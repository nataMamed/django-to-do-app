from django.contrib import admin
from .models import Task

class ListingTasks(admin.ModelAdmin):

    list_display       = ('id', 'title', 'date_created', 'complete')
    list_display_links = ('id', 'title')
    search_fields      = ('title',)
    list_filter        = ('title',)
    list_per_page      = 5

admin.site.register(Task, ListingTasks)