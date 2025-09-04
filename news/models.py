from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=255)  # Prevent duplicate titles
    summary = models.TextField(blank=True, null=True)      # <- Add this field
    source = models.CharField(max_length=255)
    published_at = models.DateTimeField()
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title
