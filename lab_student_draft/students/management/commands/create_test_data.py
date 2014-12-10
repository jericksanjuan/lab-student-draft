from django.core.management.base import NoArgsCommand
from mommy_recipes import create_test_data


class Command(NoArgsCommand):
    help = "Run create_test_data"

    def handle_noargs(self, **options):
        create_test_data()
