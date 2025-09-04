from django.contrib import admin
from .models import NewsArticle

# Register your models here.

@admin.register(NewsArticle)
class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ("title", "source", "published_at")
    search_fields = ("title", "source")
