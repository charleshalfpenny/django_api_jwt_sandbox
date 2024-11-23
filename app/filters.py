from django_filters import rest_framework as filters

from .models import Employee

class EmployeeFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='iexact')  # Case-insensitive exact match
    first_name_contains = filters.CharFilter(field_name='first_name', lookup_expr='icontains')  # Case-insensitive partial match
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='iexact')  # Case-insensitive exact match
    last_name_contains = filters.CharFilter(field_name='last_name', lookup_expr='icontains')  # Case-insensitive partial match

    class Meta:
        model = Employee
        fields = ['first_name', 'first_name_contains', 'last_name', 'last_name_contains', 'age']

