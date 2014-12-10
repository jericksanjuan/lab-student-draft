from django.core.management.base import NoArgsCommand
from mommy_recipes import update_for_phase2


class Command(NoArgsCommand):
    help = "My shiny new management command."

    def handle_noargs(self, **options):
        update_for_phase2()
