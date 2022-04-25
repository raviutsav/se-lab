from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    organisation = models.CharField(max_length=64)
    password = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} {self.email} {self.organisation} {self.password}"

