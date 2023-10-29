from django.db import models

# Create your models here.
class Job(models.Model):
    # image = models.ImageField(upload_to='images/')
    # summary = models.CharField(max_length=200)

    image = models.ImageField(upload_to='images/')
    # summary 
    summary = models.CharField(max_length=200)
    title = models.CharField(max_length=20, default="recipe-app")
    link = models.CharField(max_length=100, default='link')
    description = models.CharField(max_length= 600, default="description")
    # If anyone wants to know what's the description of this particular object is , can see the summary.
    def __str__(self):
        return self.summary