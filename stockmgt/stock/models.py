from django.db import models

# Create your models here.


class Equipment(models.Model):

    type = models.CharField(max_length=100, blank=False)
    model = models.CharField(max_length=100, blank=False)


    status = models.CharField(max_length=100, default="Available")
    issues = models.CharField(max_length=100, default="No issues")


class Meta:
    abstract = True



class Switch(Equipment):
    pass

class Ap(Equipment):
    pass

class PowerSupply(Equipment):
    pass










