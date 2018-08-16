from __future__ import unicode_literals
from django.db import models
from django.db import connection


# Create your models here.

class Album(models.Model):
    UserId = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    ImageName = models.CharField(db_column='ImageName', max_length=60)  # Field name made lowercase.
    Image = models.ImageField(upload_to='images')

class Paint(models.Model):
    UserId = models.IntegerField(db_column='UserId')  # Field name made lowercase.
    ImageName = models.CharField(db_column='PaintName', max_length=60)  # Field name made lowercase.
    Image = models.ImageField(upload_to='paint')