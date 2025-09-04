from django.core.management.base import BaseCommand
from news.utils import fetch_and_store_news

class Command(BaseCommand):
    help = "Fetch latest news articles from NewsAPI"

    def handle(self, *args, **kwargs):
        try:
            new_count = fetch_and_store_news()
            self.stdout.write(self.style.SUCCESS(f"✅ Fetched {new_count} new articles"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"⚠️ Error fetching news: {str(e)}"))
