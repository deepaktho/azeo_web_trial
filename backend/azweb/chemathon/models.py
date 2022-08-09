from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Chemathon_questions_admin(models.Model):
    q1 = RichTextField(verbose_name='Code',null=True,blank=True)
    q2 = RichTextField(verbose_name='Code',null=True,blank=True)
    q3 = RichTextField(verbose_name='Code',null=True,blank=True)
    q4 = RichTextField(verbose_name='Code',null=True,blank=True)
    q5 = RichTextField(verbose_name='Code',null=True,blank=True)
    q6 = RichTextField(verbose_name='Code',null=True,blank=True)
    q7 = RichTextField(verbose_name='Code',null=True,blank=True)

class Chemathon_questions(models.Model):
    team_id = models.CharField(max_length=100)
    question1 = models.FloatField(null=True)
    question2 = models.FloatField(null=True)
    question3 = models.FloatField(null=True)
    question4 = models.FloatField(null=True)
    question5 = models.FloatField(null=True)
    question6 = models.FloatField(null=True)
    question7 = models.FloatField(null=True)
    submitted_at = models.CharField(null=True,max_length=100)


class Chemathonuser(models.Model):
    member1 = models.CharField(max_length=100)
    member2 = models.CharField(max_length=100)
    team_id = models.CharField(max_length=100)








