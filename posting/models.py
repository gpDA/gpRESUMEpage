from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify
from ckeditor_uploader.fields import RichTextUploadingField

class CustomUser(AbstractUser):
    image = models.CharField(max_length=256, default='https://api.adorable.io/avatars/285/abott@adorable')
    email_confirmed = models.BooleanField(default=False)
    def __str__(self):
        return self.email

class Posten(models.Model):
    # 1 - M CustomUser
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    title = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    slug = models.SlugField(unique=True)
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
        super(Posten, self).save()
        
    class Meta:
        ordering = ['-timestamp','-updated']

class Postko(models.Model):

    # 1 - M CustomUser
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)      
    title = models.CharField(max_length=200, blank=True)
    number = models.IntegerField()
    slug = models.SlugField(unique=True)
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
        super(Postko, self).save()
        
    class Meta:
        ordering = ['-timestamp','-updated']        

class PostCommenten(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    post = models.ForeignKey('Posten', on_delete=models.CASCADE, related_name='post_comment_en')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text

class PostCommentko(models.Model):
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    post = models.ForeignKey('Postko', on_delete=models.CASCADE, related_name='post_comment_en')
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text        

class PostTagko(models.Model):
    post = models.ForeignKey('Postko', on_delete=models.CASCADE, related_name='project_tag_en')
    tag = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.tag    
        
class PostTagen(models.Model):
    post = models.ForeignKey('Posten', on_delete=models.CASCADE, related_name='project_tag_en')
    tag = models.CharField(max_length=100, blank=True)   

    def __str__(self):
        return self.tag    
