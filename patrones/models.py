from django.db import models


# Create your models here.
class CovidInfo(models.Model):
    date = models.CharField(max_length=8)
    positive = models.IntegerField(null=True, blank=True)
    negative = models.IntegerField(null=True, blank=True)

    @property
    def diff(self):
        if self.positive is None or self.negative is None:
            return 'No puedo realizar la operacion'
        return self.positive - self.negative