from distutils.command import upload
import email
from email import message
from email.mime import image
from email.quoprimime import quote
from operator import mod
from tabnanny import verbose
from time import time
from turtle import title
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from psycopg2 import Timestamp

# Create your models here.

class Skill(models.Model):
  class Meta:
    verbose_name_plural = 'Skills'
    verbose_name = 'Skill'
  
  name = models.CharField(max_length=20, blank=True , null=True)
  score = models.IntegerField(default=80, blank=True, null=True)
  image = models.FileField(blank=True, null=True, upload_to='skills')
  is_key_skill = models.BooleanField(default=False)

  def __str__(self):
      return self.name


class UserProfile(models.Model):
  class Meta:
    verbose_name_plural = 'User Profiles'
    verbose_name = 'User Profile'

  user = models.OneToOneField(User, on_delete=models.CASCADE)
  avatar = models.ImageField(blank=True, null=True, upload_to= 'avatar')
  title = models.CharField(max_length=150, blank=True, null=True)
  skills = models.ManyToManyField(blank=True, null=True)
  cv = models.FileField(blank=True, null=True, upload_to='cv')

  def __str__(self):
    return f'{self.user.first_name} {self.user.last_name}'

class ContactProfile(models.Model):
  class Meta:
        verbose_name_plural = 'Contact Profiles'
        verbose_name = 'Contact Profile'
        ordering = ["timestamp"]
  
  timestamp = models.DateTimeField(auto_now=True)
  name = models.CharField(verbose_name='Name', max_length=150)
  email = models.EmailField(verbose_name='Email')
  message = models.EmailField(verbose_name='Message')

  def __str__(self):
      return f'{self.name}'

class Testimonial(models.Model):

  class Meta:
    verbose_name_plural = 'Testimonials'
    verbose_name = 'Testimonial'
    orderig = ['name']

  thumbnail = models.ImageField(black=True, null=True, upload_to='testimonials')
  name = models.CharField(max_length=150, blank=True, null=True)
  role = models.CharField(max_length=150, blank=True, null=True)
  quote = models.CharField(max_length=150, blank=True, null=True)
  is_active = models.BooleanField(default=True)

  def __str__(self):
      return self.name

class Media(models.Model):

  class Meta:
    verbose_name_plural = 'Media Files'
    verbose_name = 'Media File'
    orderig = ['name']
  
  image = models.ImageField(blank=True, null=True, upload_to='media')
  url = models.URLField(blank=True, null=True)
  name =- models.CharField(max_length=150, blank=True, null=True)
  is_image = models.BooleanField(default=True)

  def save(self, *args, **kwargs):
    if self.url:
      self.is_image = False
      super(Media, self).save(*args, **kwargs)

  def __str__(self):
      return self.name
  


  
  
  
  