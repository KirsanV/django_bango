from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from catalog.models import Product


class Command(BaseCommand):
    help = 'Создает группу ProductModerators с необходимыми правами'

    def handle(self, *args, **kwargs):
        group_name = 'ProductModerators'
        group, created = Group.objects.get_or_create(name=group_name)

        ct = ContentType.objects.get_for_model(Product)

        perms = Permission.objects.filter(
            content_type=ct,
            codename__in=[
                'can_unpublish_product',
                'delete_product',
            ]
        )
        for p in perms:
            group.permissions.add(p)

        self.stdout.write(self.style.SUCCESS(f'Группа {group_name} создана/обновлена и получены права.'))