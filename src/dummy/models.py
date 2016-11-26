from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Stuff(models.Model):
    status = models.CharField(max_length=200)