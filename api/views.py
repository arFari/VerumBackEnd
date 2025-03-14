from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
import json
from api.models import News
from api.serializers import NewsSerializer
from newspaper import Article
import re

def clean_text(text):
    """
    Cleans the given text by:
    - Removing unnecessary newlines
    - Replacing multiple spaces with a single space
    - Stripping leading and trailing whitespace
    """
    text = re.sub(r'\n+', ' ', text)  # Replace multiple newlines with a space
    text = re.sub(r'\s+', ' ', text)  # Replace multiple spaces with a single space
    return text.strip() 

@csrf_exempt
def article_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        api = News.objects.all()
        serializer = NewsSerializer(api, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        article = Article(data["url"])
        article.download()
        article.parse()
        publishedAt = article.publish_date
        print(publishedAt)
        new = {
            "author": str(article.authors),
            "title": str(article.title),
            "description": str(article.summary),
            "url": data["url"],
            "urlToImage": str(article.top_image),
            "publishedAt": publishedAt,
            "content": clean_text(str(article.text))
        }
        serializer = NewsSerializer(data=new)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        article = News.objects.get(pk=pk)
    except News.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = NewsSerializer(article)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = NewsSerializer(article, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        article.delete()
        return HttpResponse(status=204)