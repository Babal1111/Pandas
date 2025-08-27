from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Chai variety model
class ChaiVarity(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'MASALA'),
        ('GR', 'GINGER'),
        ('EL', 'ELICHI'),
    ]
    name = models.CharField(max_length=100)
    # image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    description = models.TextField(default='')

    def __str__(self):
        return self.name

# Review model with one-to-many relationship to ChaiVarity
class ChaiReview(models.Model):
    chai = models.ForeignKey(ChaiVarity, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username}'s review of {self.chai.name}"

# Store model with many-to-many relationship to ChaiVarity
class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name
