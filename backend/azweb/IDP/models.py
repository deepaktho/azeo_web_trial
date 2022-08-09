from django.db import models

# Create your models here.

class IDPuser(models.Model):
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    member3 = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)

