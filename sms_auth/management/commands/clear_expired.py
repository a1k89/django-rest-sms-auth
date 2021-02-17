from django.core.management.base import BaseCommand

from ...services import CleanService


class Command(BaseCommand):
    def handle(self, *args, **options):
        CleanService.clear()



