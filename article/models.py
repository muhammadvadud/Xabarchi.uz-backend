from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Kategoriya modeli
class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Teglar modeli
class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')
    first_name = models.CharField(max_length=50)  # Izoh yozuvchining ismi
    last_name = models.CharField(max_length=50)  # Izoh yozuvchining familiyasi
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Comment by {self.first_name} {self.last_name} on {self.article}'


class Article(models.Model):
    title = models.TextField()
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    category = models.ForeignKey(Category, related_name='articles', on_delete=models.CASCADE)  # O'zgartirdik
    is_published = models.BooleanField(default=False)
    published_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return "/" + str(self.slug) + "/"

    class Meta:
        ordering = ["-id"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ArticleSection(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='sections')
    text = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='article_sections/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.article.title} - Section {self.order}"
