from django.db import models


# Create your models here.
class UserLogin(models.Model):
    email = models.EmailField(null=True)
    password = models.TextField(null=True)
