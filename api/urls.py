from django.urls import path
from api import views

urlpatterns = [
    path('snippets/', views.article_list),
    path('snippets/<int:pk>/', views.article_detail),
]