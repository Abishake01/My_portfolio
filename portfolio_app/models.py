from django.db import models
 
from django.utils import timezone

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    project_url = models.URLField(max_length=200, blank=True, null=True)
    image = models.ImageField(upload_to='project_images/', blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']  # Order by created_at, newest first
    
    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/', blank=True)
    def __str__(self):
        return self.name
    
class Contact_me(models.Model):
    User_name = models.CharField(max_length=200)
    description = models.TextField()
    link = models.URLField(max_length=200, blank=True, null=True)
    icon = models.ImageField(upload_to='contact_images/', blank=True)
    def __str__(self):
        return self.User_name

class Certificate(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='project_images/', blank=True)
    description = models.TextField()
     
    
    def __str__(self):
        return self.name

 
from django.utils.timezone import now

class Experience(models.Model):
    company_name = models.CharField(max_length=255)
    job_title = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    company_logo = models.ImageField(upload_to='experience_logos/', null=True, blank=True)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['-order', '-start_date']
    
    def __str__(self):
        return f"{self.company_name} - {self.job_title}"
    
    def get_date_range(self):
        start = self.start_date.strftime("%B %Y")
        if self.is_current:
            return f"{start} - Present"
        elif self.end_date:
            end = self.end_date.strftime("%B %Y")
            return f"{start} - {end}"
        return start