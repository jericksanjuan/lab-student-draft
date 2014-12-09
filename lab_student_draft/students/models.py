from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save

from model_utils.models import TimeStampedModel
from model_utils import Choices
from labs.models import Lab

_PICKVAL = 100

# TODO: Get minimum_groups from settings
# TODO: Get maximum groups from settings


class Batch(TimeStampedModel):
    minimum_groups = models.IntegerField(default=1)
    maximum_groups = models.IntegerField(default=10)

    class Meta:
        verbose_name = "Batch"
        verbose_name_plural = "Batches"

    def __unicode__(self):
        return u'{}-{}'.format(self.created.month, self.created.year)


class StudentGroup(TimeStampedModel):
    batch = models.ForeignKey('Batch')
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    lab = models.ForeignKey(Lab, null=True, blank=True, related_name="assigned_set")
    group_preferences = models.ManyToManyField(
        Lab, through='GroupPreference', null=True, blank=True)

    class Meta:
        verbose_name = "Student Group"
        verbose_name_plural = "Student Groups"

    def __unicode__(self):
        return u'{} group'.format(self.user)


class Student(models.Model):
    student_group = models.ForeignKey('StudentGroup')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __unicode__(self):
        return u'{} {}'.format(self.first_name, self.last_name)


class GroupPreference(models.Model):
    student_group = models.ForeignKey('StudentGroup')
    lab = models.ForeignKey(Lab)
    preference = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Group Preference"
        verbose_name_plural = "Group Preferences"
        unique_together = ('student_group', 'lab')

    def __unicode__(self):
        return u'{}={}-{}'.format(self.preference, self.student_group, self.lab)


class Selection(models.Model):
    ITERATIONS = Choices('1', '2', '3')

    lab = models.ForeignKey(Lab)
    student_group = models.ForeignKey('StudentGroup')

    phase = models.CharField(max_length=1, choices=ITERATIONS)
    is_selected = models.BooleanField(default=False)
    selection_score = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Selection"
        verbose_name_plural = "Selections"
        unique_together = ('lab', 'student_group', 'phase')

    def __unicode__(self):
        return u'{}: {}<>{}, Phase {}'.format(
            self.selection_score, self.lab,
            self.student_group, self.phase)


def update_selection_score(sender, instance, raw, *args, **kwargs):
    if raw:
        return
    self = instance
    if not (self.lab and self.student_group):
        return

    obj, _ = GroupPreference.objects.get_or_create(
        lab=self.lab, student_group=self.student_group)
    if self.is_selected:
        score = _PICKVAL + obj.preference
    else:
        score = obj.preference
    self.selection_score = score

pre_save.connect(update_selection_score, Selection, dispatch_uid='students.Selection')
