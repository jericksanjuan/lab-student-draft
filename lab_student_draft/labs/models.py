from django.conf import settings
from django.db import models


class Lab(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    selections = models.ManyToManyField(
        'students.StudentGroup', through='students.Selection',
        blank=True, null=True, related_name='+')
    batch_shares = models.ManyToManyField('students.Batch', through='Share')
    active = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"

    def __unicode__(self):
        return self.name

    @property
    def desired_groups(self):
        share = self.share_set.last()
        return share.desired_groups

    @desired_groups.setter
    def desired_groups(self, value):
        share = self.share_set.last()
        share.desired_groups = value
        share.save()

    @property
    def slots_taken(self):
        share = self.share_set.last()
        return share.slots_taken

    @slots_taken.setter
    def slots_taken(self, value):
        share = self.share_set.last()
        share.slots_taken = value
        share.save()


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
