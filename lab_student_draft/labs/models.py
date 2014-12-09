from django.conf import settings
from django.db import models


class Lab(models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    name = models.CharField(max_length=100)
    selections = models.ManyToManyField(
        'students.StudentGroup', through='students.Selection',
        blank=True, null=True, related_name='+')

    class Meta:
        verbose_name = "Lab"
        verbose_name_plural = "Labs"

    def __unicode__(self):
        return self.name
