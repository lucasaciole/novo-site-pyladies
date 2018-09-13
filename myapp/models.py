from django.db import models


# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=200)
    course = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='img/users/')
    github_link = models.CharField(max_length=200)
    facebook_link = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
