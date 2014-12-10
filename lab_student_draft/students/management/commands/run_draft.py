import math
from django.core.management.base import NoArgsCommand
from students.models import Batch, Selection, Student


class Command(NoArgsCommand):
    help = "Run the student draft for the first phase."

    def handle_noargs(self, **options):

        start_std = Student.objects.filter(
            student_group__lab=None).filter(
            student_group__batch=Batch.objects.last()).count()
        std_count = 0
        end_std = math.floor(start_std * 0.6)

        # selobjs = Selection.objects.filter(phase='1').order_by('-selection_score')
        selobjs = Selection.objects.all().order_by('-selection_score')
        selected_groups = []
        filled_labs = []

        for selx in selobjs:

            if selx.student_group.pk in selected_groups:
                continue

            if selx.lab.pk in filled_labs:
                continue

            # assign current group to lab
            selx.student_group.lab = selx.lab
            selx.student_group.save()
            std_count = std_count + selx.student_group.student_set.count()

            selected_groups.append(selx.student_group.pk)

            # remove studentgroup from selobjs
            selobjs = selobjs.exclude(student_group=selx.student_group)
            print 'removing {} from list, {}'.format(selx.student_group, selx.lab)

            # reduce available slots
            selx.lab.slots_taken = selx.lab.slots_taken + 1
            selx.lab.save()

            print selx.lab.slots_taken, selx.lab.desired_groups

            # if all slots taken, remove lab from contention
            if selx.lab.slots_taken >= selx.lab.desired_groups:
                selobjs = selobjs.exclude(lab=selx.lab)
                filled_labs.append(selx.lab.pk)
                print 'removing Lab {} from list'.format(selx.lab)

            #if the number of slots taken is at or over 60%, stop the first run.
            if std_count >= end_std:
                print 'Stopping Phase 1'
                break

