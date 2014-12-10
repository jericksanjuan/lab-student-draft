from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "My shiny new management command."

    def handle_noargs(self, **options):
        raise NotImplementedError()