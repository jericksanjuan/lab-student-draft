from django.core.management.base import NoArgsCommand

class Command(NoArgsCommand):
    help = "Run the student draft for the first and second phase."

    def handle_noargs(self, **options):
        Selection.objects.filter
