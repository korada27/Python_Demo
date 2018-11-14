from __future__ import unicode_literals
from djongo import models


class Student(models.Model):
    CreatedTimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedTimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    Name = models.CharField(max_length=20, null=True,unique=True)
    Age = models.IntegerField(null=True)
    RollNumber = models.CharField(max_length=20, null=True)

    # def __str__(self):
    #     return self.Name
