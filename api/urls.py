from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleListCreateAPIView, ArticleDetailAPIView

urlpatterns = [
    path('article/', ArticleListCreateAPIView.as_view(), name='article-list'),
    path('article/<slug:slug>/', ArticleDetailAPIView.as_view(), name='article-detail'),

]
