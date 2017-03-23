from django.contrib import admin

from employee import models


class DepartmentAdm(admin.ModelAdmin):
    pass


class EmployeeAdm(admin.ModelAdmin):
    list_display = ('name', 'department')
    list_filter = ('department',)
    search_fields = ('name',)


admin.site.register(models.Department, DepartmentAdm)
admin.site.register(models.Employee, EmployeeAdm)