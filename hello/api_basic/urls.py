from django.urls import path
from .views import article_list
from .views import book_list

urlpatterns = [
    path('article/', article_list),
    path('book/', book_list),
]
