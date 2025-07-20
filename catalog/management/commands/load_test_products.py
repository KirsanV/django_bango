from django.core.management.base import BaseCommand
from django.core.management import call_command
from catalog.models import Product, Category


class Command(BaseCommand):
    help = 'Удаляет все продукты и категории, затем загружает тестовые данные из фикстуры'

    def handle(self, *args, **kwargs):
        self.stdout.write('Удаление всех продуктов')
        Product.objects.all().delete()
        self.stdout.write('Удаление всех категорий')
        Category.objects.all().delete()

        self.stdout.write('Загрузка фикстуры catalog_fixture.json')
        call_command('loaddata', 'catalog_fixture.json')

        self.stdout.write(self.style.SUCCESS('Тестовые продукты добавлены'))
