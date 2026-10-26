from django.core.management.base import BaseCommand
from dacms_app.models import Article, Category


class Command(BaseCommand):
    help = 'Create demo data for the converted CMS'

    def handle(self, *args, **options):
        if not Category.objects.exists():
            Category.objects.create(name_en='News', name_bg='Новини', name_ru='Новости', name_de='Nachrichten', display=True, menu_order=1)
            Category.objects.create(name_en='Services', name_bg='Услуги', name_ru='Услуги', name_de='Dienste', display=True, menu_order=2)

        if not Article.objects.exists():
            Article.objects.create(
                title_en='Welcome',
                title_bg='Добре дошли',
                title_ru='Добро пожаловать',
                title_de='Willkommen',
                content_en='<p>Welcome to the Python version of DaCMS.</p>',
                content_bg='<p>Добре дошли в Python версията на DaCMS.</p>',
                content_ru='<p>Добро пожаловать в Python версию DaCMS.</p>',
                content_de='<p>Willkommen zur Python-Version von DaCMS.</p>',
                display=True,
                first_page=True,
            )

        self.stdout.write(self.style.SUCCESS('Demo data created'))
