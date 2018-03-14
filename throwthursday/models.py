from __future__ import unicode_literals

from django.db import models

class Throw(models.Model):
    name = models.CharField(max_length=250)
    points = models.IntegerField(default=0)
    matchdone = models.BooleanField(default=False)