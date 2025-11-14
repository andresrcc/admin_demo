from django.db import models
from tinymce.models import HTMLField

class Task(models.Model):
    title = models.CharField(max_length=200)
    content = HTMLField(blank=True)
    
    def __str__(self):
        return self.title
