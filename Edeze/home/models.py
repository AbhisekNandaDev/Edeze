from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class training(models.Model):
    course_name = models.CharField(max_length=100)
    course_desc = models.TextField()
    course_price = models.IntegerField()
    course_author = models.CharField(max_length=100)
    course_category = models.CharField(max_length=100,null=True)
    course_rating = models.IntegerField(null=True)

class CartTraining(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()


class Consulting(models.Model):
    consultant_id = models.IntegerField()
    cons_name= models.CharField(max_length=100)
    cons_desc = models.TextField()
    cons_price=models.IntegerField(null=True)
    cons_author = models.CharField(max_length=100)
    cons_rating = models.IntegerField()
    cons_category = models.CharField(max_length=100,null=True)


class Webstore(models.Model):
    web_name= models.CharField(max_length=100)
    web_desc = models.TextField()
    web_price=models.IntegerField(null=True)
    web_author = models.CharField(max_length=100)
    web_rating = models.IntegerField()
    web_category = models.CharField(max_length=100,null=True)

class CartWebstore(models.Model):
    user_id = models.IntegerField()
    course_id = models.IntegerField()

