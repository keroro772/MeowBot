from __future__ import unicode_literals

from django.db import models

class Clip(models.Model):
    game = models.CharField(max_length=100)
    name = models.CharField(max_length=250)
    link = models.CharField(max_length=500)
    def __str__(self):
        return '{} : {}'.format(self.game, self.link)