from unicodedata import name
from django.db import models
from super_types.models import Super_Type

class Power(models.Model):
    name = models.CharField(max_length=75)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Super(models.Model):
    name = models.CharField(max_length=75)
    alter_ego = models.CharField(max_length=75)
    powers = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=75)
    super_type = models.ForeignKey(Super_Type, on_delete=models.CASCADE)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
