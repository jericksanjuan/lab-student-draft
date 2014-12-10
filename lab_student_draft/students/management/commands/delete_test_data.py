from django.core.management.base import NoArgsCommand
from mommy_recipes import delete_test_data


class Command(NoArgsCommand):
    help = "Run delete_test_data"

    def handle_noargs(self, **options):
        delete_test_data()
