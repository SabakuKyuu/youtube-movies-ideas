from django.contrib import admin
from .models import Idea, Vote
from django.utils.html import format_html

class VoteInLine(admin.TabularInline):
    model = Vote

class VoteInLine2(admin.StackedInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'status', 'show_youtube_url']
    list_filter = ['status']

    def show_youtube_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a href="{obj.youtube_url}">{obj.youtube_url}</a>')

    show_youtube_url.short_description = 'URL'

    inlines = [VoteInLine]

@admin.register(Vote)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea', 'reason']
    list_filter = ['idea']