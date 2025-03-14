from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]


class News(models.Model):
    author = models.TextField(blank=False, default='')
    title = models.TextField()
    description = models.TextField(blank=True)
    url = models.TextField()
    urlToImage = models.TextField(blank=True)
    publishedAt = models.DateTimeField(blank=True, null=True)
    content = models.TextField()

    class Meta:
        ordering = ['publishedAt']