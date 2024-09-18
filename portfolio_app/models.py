from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Contact_me(models.Model):
    User_name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='contact_images/', blank=True)

    def __str__(self):
        return self.User_name
 