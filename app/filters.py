from django_filters import rest_framework as filters

from .models import Employee

class EmployeeFilter(filters.FilterSet):
    first_name = filters.CharFilter(field_name='first_name', lookup_expr='iexact')  # Case-insensitive exact match
    first_name_contains = filters.CharFilter(field_name='first_name', lookup_expr='icontains')  # Case-insensitive partial match
    last_name = filters.CharFilter(field_name='last_name', lookup_expr='iexact')  # Case-insensitive exact match
    last_name_contains = filters.CharFilter(field_name='last_name', lookup_expr='icontains')  # Case-insensitive partial match

    age = filters.NumberFilter(field_name='age')  # Exact match
    age_gt = filters.NumberFilter(field_name='age', lookup_expr='gt')  # Greater than
    age_lt = filters.NumberFilter(field_name='age', lookup_expr='lt')  # Less than
    age_gte = filters.NumberFilter(field_name='age', lookup_expr='gte')  # Greater than or equal
    age_lte = filters.NumberFilter(field_name='age', lookup_expr='lte')  # Less than or equal


    class Meta:
        model = Employee
        fields = ['first_name', 'first_name_contains', 'last_name', 'last_name_contains', 'age']

