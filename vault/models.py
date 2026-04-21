from django.db import models

# Create your models here.
class Link(models.Model):
    url = models.URLField()
    title = models.CharField(max_length=255)
    tag = models.CharField(max_length=100)

    def __str__(self):
        return self.title