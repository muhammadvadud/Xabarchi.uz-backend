from django.contrib import admin
from .models import ArticleSection, Article, Comment, Tag, Category


class ArticleSectionInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = ArticleSection
    extra = 1  # Yana qanchta bo'sh maydon ko'rsatish kerak


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'is_published')  # Ko'rsatish kerak bo'lgan maydonlar
    inlines = [ArticleSectionInline]  # ArticleSection inline qo'shish


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSection)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
