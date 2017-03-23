import json
from django.http import HttpResponse
from employee import models
from django.shortcuts import render


# Create your views here.

def employees(request):
    employees = models.Employee.objects.all().select_related('department')

    result = []

    for employee in employees:
        result.append(dict(
            name=employee.name,
            email=employee.email,
            department=employee.department.name,
        ))

    return HttpResponse(
        json.dumps(result),
        content_type='application/json')
