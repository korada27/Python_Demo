# from django.db import models
# Create your models here.
from __future__ import unicode_literals
from djongo import models


class Employee(models.Model):
    Name = models.CharField(max_length=20, null=True)
    Age = models.IntegerField(null=True)
    EmpId = models.CharField(max_length=20, null=True)
    Email = models.CharField(max_length=30, null=True, unique=True)
    Password = models.CharField(max_length=15, null=True)
    Salary = models.BigIntegerField(null=True, default='null')
    City = models.CharField(max_length=15, null=True, default='null')
    CreatedTimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    UpdatedTimeStamp = models.DateTimeField(auto_now_add=True, auto_now=False)

    class Meta:
        verbose_name = u'Employee'
        verbose_name_plural = u'Employees'

    def __unicode__(self):
        return self.Name
