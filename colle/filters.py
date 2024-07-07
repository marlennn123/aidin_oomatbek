from django_filters.rest_framework import FilterSet
from .models import Department, Professor, Student, Cours

class DepartmentFilter(FilterSet):
    class Meta:
        model = Department
        fields = {
            'name': ['exact'],
        }

class ProfessorFilter(FilterSet):
    class Meta:
        model = Professor
        fields = {
            'user': ['exact'],
        }

class StudentFilter(FilterSet):
    class Meta:
        model = Student
        fields = {
            'user': ['exact'],

        }
class CoursFilter(FilterSet):
    class Meta:
        model = Cours
        fields = {
            'name': ['exact'],
            'price': ['gt', 'lt'],
        }