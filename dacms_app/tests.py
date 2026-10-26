from django.test import TestCase
from django.urls import reverse
from dacms_app.models import Category, Article


class CmsSmokeTests(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            name_en='News',
            name_bg='Новини',
            name_ru='Новости',
            name_de='Nachrichten',
            slug='news',
            display=True,
            menu_order=1,
        )
        self.article = Article.objects.create(
            title_en='Welcome',
            title_bg='Добре дошли',
            title_ru='Добро пожаловать',
            title_de='Willkommen',
            slug='welcome',
            content_en='Hello world',
            display=True,
            first_page=True,
        )

    def test_home_page_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_category_page_loads(self):
        response = self.client.get(reverse('category_detail', args=[self.category.slug]))
        self.assertEqual(response.status_code, 200)

    def test_article_page_loads(self):
        response = self.client.get(reverse('article_detail', args=[self.article.slug]))
        self.assertEqual(response.status_code, 200)
