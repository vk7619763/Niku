from django.contrib import admin

# Register your models here.
from testapp.models import employee

class employeeadmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','ecity']

admin.site.register(employee,employeeadmin)
