#filename models.py
from django.db import models

class author(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
