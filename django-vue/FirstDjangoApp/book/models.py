from django.db import models

# Create your models here.
class Book(models.Model):
    tittle = models.CharField(max_length = 50)
    description = models.TextField()
    pages = models.IntegerField()