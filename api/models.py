from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]


class Article(models.Model):
    author = models.CharField(max_length=100, blank=False, default='')
    title = models.TextField()
    description = models.TextField()
    url = models.TextField()
    urlToImage = models.TextField()
    publishedAt = models.DateTimeField()
    content = models.TextField()

    class Meta:
        ordering = ['publishedAt']