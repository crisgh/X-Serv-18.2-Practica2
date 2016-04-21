from __future__ import unicode_literals

from django.db import models

# Create your models here.
class URL(models.Model):
    original = models.TextField()
    cortada = models.IntegerField()
