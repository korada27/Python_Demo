from rest_framework import serializers
from .import models


class AddStudentSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('Name', 'Age', 'RollNumber')
        model = models.Student
