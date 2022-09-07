
from msilib.schema import Feature
from pydoc import describe
from sre_constants import CATEGORY
from turtle import update
from django.db import models
from django.utils.translation import gettext_lazy as _ 
from django.conf import settings
from django.contrib.auth.models import User



class Category(models.Model):
    title=models.CharField(verbose_name=_("title"),max_length=255)
    active=models.BooleanField(verbose_name=_("active"))
    # created_time=models.DateTimeField(auto_now_add=True)
    # updated_time=models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.title


    class Meta:
        verbose_name=_("category")
        verbose_name_plural=_("categories")


class Post(models.Model):

    class StatusChoices(models.TextChoices):
        DRAFT= _("draft")
        PUBLISHED= _("published")


    title=models.CharField(verbose_name=_("title"),max_length=255)
    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True)
    body=models.TextField(verbose_name=_("body"))
    is_enabled=models.BooleanField(default=False )
    author=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,blank=True)
    created_time=models.DateTimeField(verbose_name=_("created_time"),auto_now_add=True)
    updeted_time=models.DateTimeField(verbose_name=_("updeted_time"),auto_now=True)
    status=models.CharField(verbose_name=_("status"),max_length=15,choices= StatusChoices.choices,default=StatusChoices.DRAFT)
    publish_time=models.DateTimeField(verbose_name=_("publish_time"),null=True,blank=True)
    Featured=models.BooleanField(verbose_name=_("Featured"),null=True)
    likes=models.ManyToManyField(User,related_name="bloglikes",blank=True)



    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name=_("post")
        verbose_name_plural=_("posts")



      
class Comment(models.Model):
    Post=models.ForeignKey(Post,on_delete=models.CASCADE)
    text=models.TextField()
    # created_time=models.DateTimeField(auto_now_add=True)
    # updated_time=models.DateTimeField(auto_now=True)
