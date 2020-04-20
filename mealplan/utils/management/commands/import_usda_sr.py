from django.core.management.base import BaseCommand, CommandError

from utils.usda import import_ingredients


class Command(BaseCommand):
    help = 'Imports USDA Standard Reference (SR) ingredients from csv files'

    def handle(self, *args, **options):
        import_ingredients()
        self.stdout.write(self.style.SUCCESS(
            'Successfully imported all USDA SR ingredients'))
