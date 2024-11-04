from django.contrib import admin
from .models import Article, ArticleSection, Comment, Tag, Category


class ArticleSectionInline(admin.TabularInline):  # Yoki admin.StackedInline
    model = ArticleSection
    extra = 1  # Yana qanchta bo'sh maydon ko'rsatish kerak


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')  # Ko'rsatish kerak bo'lgan maydonlar
    inlines = [ArticleSectionInline]  # ArticleSection inline qo'shish
    filter_horizontal = ('tags',)  # Taglarni tanlashda osonlik yaratadi


admin.site.register(Article, ArticleAdmin)
admin.site.register(ArticleSection)
admin.site.register(Comment)
admin.site.register(Tag)
admin.site.register(Category)
