from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from user_management.models import Employee
# Create your views here
# Actual Business Logic
# CRUD ---> Create(http method is POST)
# CRUD ---> Read(http method is GET)
# CRUD ---> Update(http method is PUT/PATCH)
# CRUD ---> Delete(http method is DELETE)

class EmployeesDetails(generics.GenericAPIView):
    def get_queryset(self):
        return Employee.objects.all()

    def get(self, request, *args, **kwargs):
        emp_qs = self.get_queryset()
        emp_dct = [] 
        for emp in emp_qs:
           temp = {}
           temp['emp_id'] = emp.emp_id
           temp['name'] = emp.name
           temp['age'] = emp.age
           temp['gender'] = emp.gender
           emp_dct.append(temp)
        return Response(emp_dct, status=status.HTTP_200_OK)
    

class EmployeesDetailView(generics.GenericAPIView):
    def get_queryset(self,id):
        return Employee.objects.get(id=id)

    def get(self, request, id, *args, **kwargs):
        emp = self.get_queryset(id)

        temp = {}
        temp['emp_id'] = emp.emp_id
        temp['name'] = emp.name
        temp['age'] = emp.age
        temp['gender'] = emp.gender

        return Response(temp, status=status.HTTP_200_OK)
