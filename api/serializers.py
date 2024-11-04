from rest_framework import serializers
from article.models import Article, ArticleSection, Category, Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class ArticleSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSection
        fields = ['text', 'image', 'order', ]


class ArticleSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'published_date', 'category']

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        article = Article.objects.create(**validated_data)
        for section_data in sections_data:
            ArticleSection.objects.create(article=article, **section_data)
        return article


class ArticleDetailSerializer(serializers.ModelSerializer):
    sections = ArticleSectionSerializer(many=True)
    tags = TagSerializer(many=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'published_date', 'category', 'tags', 'sections']

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        article = Article.objects.create(**validated_data)
        for section_data in sections_data:
            ArticleSection.objects.create(article=article, **section_data)
        return article


class CategorySerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True, source='category.title')  # Category'dan articles olish

    class Meta:
        model = Category
        fields = ['id', 'name', 'articles']
