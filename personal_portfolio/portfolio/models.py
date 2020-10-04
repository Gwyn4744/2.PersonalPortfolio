from django.db import models
from datetime import date

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    date = models.DateField(default=date.today)

    def __str__(self):
        return self.title