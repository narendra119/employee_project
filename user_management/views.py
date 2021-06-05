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
    
    def post(self, request, *args, **kwargs):
        query_params = request.query_params

        name = query_params.get('name')
        age = query_params.get('age')
        emp_id = query_params.get('emp_id')
        gender = query_params.get('gender')

        emp_instance = Employee.objects.create(name=name, emp_id=emp_id, gender=gender, age=age)
        emp_instance.save()

        return Response('employee created successfully', status=status.HTTP_201_CREATED)

    

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
    
    def check(self):
        return "hello hi"

    def delete(self, request,id,*args, **kwargs):
        emp = self.get_queryset(id)
        
        print(type(emp))
        return Response('deactivate', status=status.HTTP_200_OK)
