from django.db import models

class Catnip(models.Model):
    name = models.CharField(max_length=250)
    amount = models.IntegerField()
    currentAmount = models.IntegerField()
    def __str__(self):
        return 'Name:{} | Amount:{}'.format(self.name, str(self.amount))

