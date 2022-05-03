from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=250)
    Email_id=models.CharField(max_length=250)
    Role=models.CharField(max_length=250)
    mobile_no=models.IntegerField()


