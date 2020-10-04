from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to='blog/images/', default='blog/images/rpi.png')
    date = models.DateField()

    def __str__(self):
        return self.title