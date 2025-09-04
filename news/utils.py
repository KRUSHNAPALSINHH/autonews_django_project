import requests
from django.conf import settings
from .models import NewsArticle
from datetime import datetime

def fetch_and_store_news():
    api_key = settings.NEWS_API_KEY
    url = f"https://newsapi.org/v2/top-headlines?country=us&category=technology&apiKey={api_key}"



    response = requests.get(url)
    data = response.json()

    # Debug: print status and number of articles
    print("API Status:", data.get("status"))
    print("Total Results:", data.get("totalResults"))
    print("Articles Returned:", len(data.get("articles", [])))

    new_count = 0
    for article in data.get("articles", []):
        title = article.get("title")
        summary = article.get("description", "")
        source = article.get("source", {}).get("name", "Unknown")
        published_at = article.get("publishedAt")
        url = article.get("url")

        print("Checking article:", title)

        if not NewsArticle.objects.filter(url=url).exists():
            NewsArticle.objects.create(
                title=title,
                summary=summary,
                source=source,
                published_at=datetime.fromisoformat(published_at.replace("Z", "+00:00")),
                url=url,
            )
            new_count += 1
            print("✅ Added:", title)
        else:
            print("⚠️ Skipped duplicate:", url)

    print("Done. New articles saved:", new_count)
    return new_count
