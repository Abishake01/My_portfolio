from django.db import models
 
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/', blank=True)
    def __str__(self):
        return self.name

class Certificate(models.Model):
    image = models.ImageField(upload_to='project_images/', blank=True)
    description = models.TextField()
     
    
    def __str__(self):
        return self.description
