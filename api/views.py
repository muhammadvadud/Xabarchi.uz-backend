from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView, ListAPIView
from api.serializers import ArticleSerializer, ArticleDetailSerializer, TagSerializer, CategorySerializer
from article.models import Article, Category, Tag, Comment


class ArticleListCreateAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field = 'slug'

    def get_queryset(self):
        slug = self.kwargs['slug']
        return Article.objects.filter(slug=slug)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryArticleView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'


class TagList(ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
