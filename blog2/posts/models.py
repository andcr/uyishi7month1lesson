from django.db import models
from time import timezone
# Create your models here.
class Post(models.Model):
     title = models.CharField(max_length=200)
     text = models.TextField()
     published_date = models.DateTimeField(blank=True, null=True)