from rest_framework import serializers
from api.models import News


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ['id', 'author', 'title', 'description', 'url', 'urlToImage', 'publishedAt', 'content']
    publishedAt = serializers.DateTimeField(allow_null=True, required=False)