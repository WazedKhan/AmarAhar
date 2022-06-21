from django.db import models
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    image = models.ImageField(upload_to = 'Account')
    experience = models.DecimalField(max_digits=1, null=True, blank=True)
    type = models.CharField(max_length=100)