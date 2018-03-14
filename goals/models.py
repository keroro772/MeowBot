from __future__ import unicode_literals

from django.db import models

class goals(models.Model):
    name = models.CharField(max_length=250)
    desc = models.CharField(max_length=500)
    price = models.IntegerField()
    total = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def percent(self):
        return str(100 * (float(self.total)/float(self.price)))
    
    percent = property(percent)