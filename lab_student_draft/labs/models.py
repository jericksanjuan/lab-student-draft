from django.conf import settings
from django.db import models


class Lab(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    selections = models.ManyToManyField(
        'students.StudentGroup', through='students.Selection',
        blank=True, null=True, related_name='+')
    batch_shares = models.ManyToManyField('students.Batch', through='Share')

    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"

    def __unicode__(self):
        return self.name


class Share(models.Model):
    lab = models.ForeignKey('Lab')
    batch = models.ForeignKey('students.Batch')

    slots_taken = models.IntegerField(default=0)
    desired_groups = models.IntegerField(default=1)

    class Meta:
        verbose_name = "Share"
        verbose_name_plural = "Shares"

    def __unicode__(self):
        return u"{}{} {} of {}".format(
            self.lab, self.batch, self.slots_taken, self.desired_groups)
