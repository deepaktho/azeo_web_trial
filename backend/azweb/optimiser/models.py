from django.db import models

# Create your models here.

class Optimiseruser(models.Model):
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)
    user_id = models.CharField(max_length=100, default='0000000')
