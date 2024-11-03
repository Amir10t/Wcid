from django.db import models

# Create your models here.

class TestModel(models.Model):
    a = models.CharField(max_length=200)
