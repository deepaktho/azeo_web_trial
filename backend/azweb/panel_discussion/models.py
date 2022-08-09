from django.db import models

# Create your models here.
class Panel_discussionuser(models.Model):
    member1 = models.CharField(max_length=100)
