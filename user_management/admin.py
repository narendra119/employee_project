from django.contrib import admin
from user_management.models import Employee
from user_management.models import Organisation,employee_Details

# Register your models here.
admin.site.register(Employee)
admin.site.register(Organisation)
admin.site.register(employee_Details)