from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length=150)
    author = models.CharField(max_length=50,default='admin')
    body = models.TextField()
    timestamp = models.DateTimeField()
    def __str__(self):
        return self.title#now we choose the way from web, but I think the way book had is more beautiful
    class Meta:
        ordering = ['-timestamp']
class Article(models.Model):
    cover = models.ImageField(upload_to='article_cover',default='/article_cover/mo/normal.jpg')
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    simple_production = models.CharField(max_length=200,default='')
    title= models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    Article_id = models.IntegerField()
    markdown = models.FileField(upload_to='article_markdown')
    tags = models.CharField(max_length=30,default='')
    click = models.IntegerField(default=0)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-timestamp']

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    idnumber = models.IntegerField(default=1)
    phone = models.CharField(max_length=30)
    avatar = models.ImageField(upload_to='photo')
    def __str__(self):
        return self.user.username
class Comment(models.Model):
    timestamp = models.DateTimeField(default=datetime.datetime.now())
    witharticle = models.IntegerField(default=-1)
    father = models.IntegerField(default = 0)
    floor = models.IntegerField(default = 0)
    author = models.CharField(max_length=50,default='admin')
    content = models.TextField(default='hi~')
    def __str__(self):
        return self.author+"   "
        class Meta:
            ordering = ['floor']
