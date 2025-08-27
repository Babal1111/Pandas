from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField()
    content = models.TextField()
    date = models.DateField()
    author = models.CharField(max_length=10)

    # def __str__(self):  
    #     return self.title
