from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.db.models import OneToOneField


# Create your models here.
class Blogger(models.Model):
    user = OneToOneField(User , on_delete=models.DO_NOTHING , default=1)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/bloggers/%Y/%m/%d/')
    birth_date = models.DateTimeField(default=datetime.now , blank=True)
    register_date = models.DateTimeField(default=datetime.now , blank=True)
    posts_count = models.IntegerField(default=0)
    description = models.TextField()
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)


    def __str__(self):
        return self.name


