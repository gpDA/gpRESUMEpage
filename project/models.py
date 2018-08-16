from django.db import models
from posting.models import CustomUser
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField


class Projecten(models.Model):
    # 1 - M CustomUser
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(config_name='default', null=True)
    order = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Projecten, self).save()
        
    class Meta:
        ordering = ['-timestamp','-updated']

class Projectko(models.Model):

    # 1 - M CustomUser
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)      
    title = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    slug = models.SlugField(unique=True)
    tag = models.CharField(max_length=100, blank=True)
    content = RichTextUploadingField(config_name='default', null=True)
    order = models.IntegerField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Projectko, self).save()
        
    class Meta:
        ordering = ['-timestamp','-updated']   