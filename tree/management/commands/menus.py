from django.core.management import BaseCommand, call_command

from tree.models import Menu, MenuName


class Command(BaseCommand):
    help = 'Загружает данные в бд'

    def handle(self, *args, **options):

        if not MenuName.objects.all().exists():
            call_command('loaddata', 'menuname', verbosity=0)
            print('Загрузка меню')
        if not Menu.objects.all().exists():
            call_command('loaddata', 'menu', verbosity=0)
            print('Загрузка MenuItem')