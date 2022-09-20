from errno import EDEADLK
import mailbox
from django.db import models

# Create your models here.
class Editor(models.Model):
    username = models.CharField(max_length=30)
    mail = models.EmailField()
    cantIdeas = models.IntegerField(default=0)
    edad = models.IntegerField()

class Lector(models.Model):
    username = models.CharField(max_length=30)
    mail = models.EmailField()
    cantVals = models.IntegerField(default=0)
    edad = models.IntegerField()

class Ideas(models.Model):
    tema = models.CharField(max_length=30)
    autor = Editor()
    texto = models.CharField(max_length=280)
    cantVals = models.IntegerField(default=0)
    puntos = models.IntegerField(default=0)
    datetimePubl = models.DateTimeField()