from rest_framework import serializers
from api.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content']