from django.db import models
from django.contrib.auth.models import AbstractUser

from .utils import localized_value


class User(AbstractUser):
    pass


class Language(models.Model):
    english = models.BooleanField(default=False)
    bulgarian = models.BooleanField(default=False)
    russian = models.BooleanField(default=False)
    deutsch = models.BooleanField(default=False)

    def __str__(self):
        return f"Language {self.id}"


class Category(models.Model):
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_bg = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    display = models.BooleanField(default=True)
    menu_order = models.IntegerField(blank=True, null=True)

    @property
    def name(self):
        return localized_value(self.name_en, self.name_bg, self.name_ru, self.name_de, 'en')

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.name_en or self.name_bg or self.name_ru or self.name_de or 'category'
            self.slug = base.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name or str(self.id)


class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subcategories', null=True, blank=True)
    name_en = models.CharField(max_length=255, blank=True, null=True)
    name_bg = models.CharField(max_length=255, blank=True, null=True)
    name_ru = models.CharField(max_length=255, blank=True, null=True)
    name_de = models.CharField(max_length=255, blank=True, null=True)
    display = models.BooleanField(default=True)
    menu_order = models.IntegerField(blank=True, null=True)
    enable_box = models.BooleanField(default=False)
    image_box = models.CharField(max_length=255, blank=True, null=True)
    subtitle_box = models.TextField(blank=True, null=True)
    enable_header = models.BooleanField(default=False)
    image_header = models.CharField(max_length=255, blank=True, null=True)

    @property
    def name(self):
        return localized_value(self.name_en, self.name_bg, self.name_ru, self.name_de, 'en')

    def __str__(self):
        return self.name or str(self.id)


class CategoryRelationship(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_relationships', null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, related_name='category_relationships', null=True, blank=True)


class Article(models.Model):
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_bg = models.CharField(max_length=255, blank=True, null=True)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_de = models.CharField(max_length=255, blank=True, null=True)
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
    url_title_en = models.CharField(max_length=255, blank=True, null=True)
    url_title_bg = models.CharField(max_length=255, blank=True, null=True)
    url_title_ru = models.CharField(max_length=255, blank=True, null=True)
    url_title_de = models.CharField(max_length=255, blank=True, null=True)
    content_en = models.TextField(blank=True, null=True)
    content_bg = models.TextField(blank=True, null=True)
    content_ru = models.TextField(blank=True, null=True)
    content_de = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=True)
    first_page = models.BooleanField(default=False)

    @property
    def title(self):
        return localized_value(self.title_en, self.title_bg, self.title_ru, self.title_de, 'en')

    def save(self, *args, **kwargs):
        if not self.slug:
            base = self.title_en or self.title_bg or self.title_ru or self.title_de or 'article'
            self.slug = base.lower().replace(' ', '-')
        super().save(*args, **kwargs)

    @property
    def url_title(self):
        return localized_value(self.url_title_en, self.url_title_bg, self.url_title_ru, self.url_title_de, 'en')

    @property
    def content(self):
        return localized_value(self.content_en, self.content_bg, self.content_ru, self.content_de, 'en')

    def __str__(self):
        return self.title or str(self.id)


class ArticleRelation(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='related_articles', null=True, blank=True)
    related_article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='reverse_related_articles', null=True, blank=True)


class CSS(models.Model):
    content = models.TextField(blank=True, null=True)


class CategoryLink(models.Model):
    title_en = models.CharField(max_length=255, blank=True, null=True)
    title_bg = models.CharField(max_length=255, blank=True, null=True)
    title_ru = models.CharField(max_length=255, blank=True, null=True)
    title_de = models.CharField(max_length=255, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='links')
    subcategory = models.ForeignKey('SubCategory', on_delete=models.SET_NULL, null=True, blank=True, related_name='links')

    @property
    def title(self):
        return localized_value(self.title_en, self.title_bg, self.title_ru, self.title_de, 'en')


class LinkContent(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    category_link = models.ForeignKey(CategoryLink, on_delete=models.CASCADE, related_name='contents', null=True, blank=True)


class Album(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    display = models.BooleanField(default=True)


class Photo(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='photos/', blank=True, null=True)
    display = models.BooleanField(default=True)


class Carousel(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    display = models.BooleanField(default=True)


class CarouselPhoto(models.Model):
    carousel = models.ForeignKey(Carousel, on_delete=models.CASCADE, related_name='photos', null=True, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='carousel/', blank=True, null=True)
    display = models.BooleanField(default=True)


class LanguageAdmin(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)


class BotSearch(models.Model):
    query = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class BotSearchResult(models.Model):
    bot_search = models.ForeignKey(BotSearch, on_delete=models.CASCADE, related_name='results', null=True, blank=True)
    result = models.TextField(blank=True, null=True)


class Theme(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    css = models.TextField(blank=True, null=True)
