from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Employee
    fields = ['id', 'last_name', 'first_name', 'age']