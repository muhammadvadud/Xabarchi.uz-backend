from rest_framework import serializers
from article.models import Article, ArticleSection


class ArticleSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleSection
        fields = ['text', 'image', 'order']


class ArticleSerializer(serializers.ModelSerializer):
    sections = ArticleSectionSerializer(many=True)

    class Meta:
        model = Article
        fields = ['id', 'title', 'slug', 'published_date', 'sections']

    def create(self, validated_data):
        sections_data = validated_data.pop('sections')
        article = Article.objects.create(**validated_data)
        for section_data in sections_data:
            ArticleSection.objects.create(article=article, **section_data)
        return article
