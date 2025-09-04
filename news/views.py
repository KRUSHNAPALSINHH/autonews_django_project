from django.shortcuts import render, redirect
from django.contrib import messages
from .models import NewsArticle
from .utils import fetch_and_store_news

def dashboard(request):
    articles = NewsArticle.objects.all().order_by('-published_at')
    return render(request, "news/dashboard.html", {"articles": articles})

def fetch_news_view(request):
    """Manual fetch triggered by button"""
    new_count = fetch_and_store_news()
    messages.success(request, f"✅ {new_count} new articles fetched!")
    return redirect("dashboard")
