from django.urls import path
from .views import ArticleListAPIView, ArticleDetailAPIView, CategoryArticleView, CategoryListView, ArticleSearchView

urlpatterns = [
    path('news/', ArticleListAPIView.as_view(), name='article-list'),
    path('news/<slug:slug>/', ArticleDetailAPIView.as_view(), name='article-detail'),
    path('search/', ArticleSearchView.as_view(), name='article-search'),
    # Ushbu qator muhim
    path('category/', CategoryListView.as_view(), name='article-list'),
    path('category/<str:name>/', CategoryArticleView.as_view(), name='category-detail'),
]
