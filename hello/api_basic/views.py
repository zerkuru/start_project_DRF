from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .models import Book
from .serializers import ArticleSerializer
from .serializers import BookSerializer

# Create your views here.

def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return JSONParser(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)



def book_list(request):

    if request.method == 'GET':
        articles = Book.objects.all()
        serializer = BookSerializer(articles, many=True)
        return JSONParser(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        else:
            return JSONResponse(serializer.errors, status=400)

