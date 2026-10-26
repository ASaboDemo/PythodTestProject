from rest_framework import serializers
from .models import Article, Category, Album


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name_en', 'name_bg', 'name_ru', 'name_de', 'slug', 'display', 'menu_order']


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'title_en', 'title_bg', 'title_ru', 'title_de', 'slug', 'content_en', 'content_bg', 'content_ru', 'content_de', 'display', 'first_page']


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ['id', 'title', 'description', 'display']
