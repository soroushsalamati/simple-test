from django.db import models
from django.contrib.auth.models import User

class Poster(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    is_sale = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)