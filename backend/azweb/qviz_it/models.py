from django.db import models

# Create your models here.

class Qviz_it_iitb(models.Model):
    member1 = models.CharField(max_length=100)

class Qviz_it_noniitb(models.Model):
    member1 = models.CharField(max_length=100)
