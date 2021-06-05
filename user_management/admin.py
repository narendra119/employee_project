from django.contrib import admin
from user_management.models import Employee
from user_management.models import Organisation

# Register your models here.
admin.site.register(Employee)
admin.site.register(Organisation)