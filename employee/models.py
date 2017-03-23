from __future__ import unicode_literals

from django.db import models


# Departamento
class Department(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

# Funcionarios
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(Department)

    def __str__(self):
        return self.name