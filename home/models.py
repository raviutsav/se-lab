from xml.dom.minidom import Document
from django.db import models

# Create your models here.

class Users(models.Model):
    name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    organisation = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    account_type = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} {self.email} {self.organisation} {self.password} {self.account_type}"


class conference(models.Model):
    con_name = models.CharField(max_length=64)
    host_organisation = models.CharField(max_length=64)
    start_date = models.CharField(max_length=64)
    end_date = models.CharField(max_length=64)

    def __self__(self):
        return f"{self.con_name}{self.host_organisation} {self.start_date} {self.end_date}"


# class submissions(models.Model):
#     submitter_name: models.CharField(max_length=64)
#     conference_name: models.CharField(max_length=64)
#     document: models.FileField()

#     def __self__(self):
#         return f"{self.submitter_name} {self.conference_name}"
