from django import forms
from .models import Album, Article, Carousel, Category, CategoryLink, SubCategory, Theme


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name_en', 'name_bg', 'name_ru', 'name_de', 'display', 'menu_order']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = [
            'category', 'name_en', 'name_bg', 'name_ru', 'name_de',
            'display', 'menu_order', 'enable_box', 'image_box', 'subtitle_box',
            'enable_header', 'image_header'
        ]


class CategoryLinkForm(forms.ModelForm):
    class Meta:
        model = CategoryLink
        fields = ['category', 'subcategory', 'title_en', 'title_bg', 'title_ru', 'title_de', 'url']


class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'display']


class CarouselForm(forms.ModelForm):
    class Meta:
        model = Carousel
        fields = ['title', 'display']


class ThemeForm(forms.ModelForm):
    class Meta:
        model = Theme
        fields = ['name', 'css']


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = [
            'title_en', 'title_bg', 'title_ru', 'title_de',
            'url_title_en', 'url_title_bg', 'url_title_ru', 'url_title_de',
            'content_en', 'content_bg', 'content_ru', 'content_de',
            'display', 'first_page'
        ]
