from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from user_management.models import Employee, Organisation
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
# Create your views here
# Actual Business Logic
# CRUD ---> Create(http method is POST)
# CRUD ---> Read(http method is GET)
# CRUD ---> Update(http method is PUT/PATCH)
# CRUD ---> Delete(http method is DELETE)

class EmployeesDetails(APIView):
    def get_queryset(self):
        return Employee.objects.all()

    def get(self, request, *args, **kwargs):
        emp_qs = self.get_queryset()
        emp_ser=EmployeeSerializer(emp_qs, many=True)
        result=emp_ser.data
        # emp_dct = [] 
        # for emp in emp_qs:
        #    temp = {}
        #    temp['emp_id'] = emp.emp_id
        #    temp['name'] = emp.name
        #    temp['age'] = emp.age
        #    temp['gender'] = emp.gender
        #    emp_dct.append(temp)

        return Response(result, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        query_params = request.query_params

        name = query_params.get('name')
        age = query_params.get('age')
        emp_id = query_params.get('emp_id')
        gender = query_params.get('gender')

        emp_instance = Employee.objects.create(name=name, emp_id=emp_id, gender=gender, age=age)
        emp_instance.save()

        return Response('employee created successfully', status=status.HTTP_201_CREATED)

    

class EmployeesDetailView(APIView):
    def get_queryset(self,id):
        return Employee.objects.get(id=id)

    def get(self, request, id, *args, **kwargs):
        #temp = {}
        try:
            emp = Employee.objects.get(id=id)
            emp_ser=EmployeeSerializer(emp)
            data=emp_ser.data
            # temp['emp_id'] = emp.emp_id
            # temp['name'] = emp.name
            # temp['age'] = emp.age
            # temp['gender'] = emp.gender
        
        except Employee.DoesNotExist as e:
            temp['error'] = "chusukovale ga bro"
            
            return Response(temp, status=status.HTTP_404_NOT_FOUND)

        return Response(data, status=status.HTTP_200_OK)


    def delete(self, request,id,*args, **kwargs):
        emp = self.get_queryset(id)
        
        
        return Response('deactivate', status=status.HTTP_200_OK)

    def put(self, request,id,*args, **kwargs):

        age=request.data['age']
        name=request.data['test']
        # import ipdb; ipdb.set_trace()
        try:
            emp = Employee.objects.get(id=id)
            emp.age=age
            emp.name=name
            emp.save()
            
        except Employee.DoesNotExist:
            result = {}
            result["error"]=f"Kallu mingaya {id} ledhu"
            return Response(result, status=status.HTTP_404_NOT_FOUND)


        return Response('Details Updated', status=status.HTTP_200_OK)

class OrganisationDetails(APIView):

    def get_queryset(self,id):
        return Organisation.objects.get(id=id)
    
    def get(self,request,id,*args,**kwargs):
        org = self.get_queryset(id)
        
        emporg = {}
        emporg["headQuarters"] = org.headQuarters
        emporg["branch"] = org.branch
        emporg["branch_Address"] = org.branch_Address
        emporg["employee_ID"] = org.employee_ID
        emporg["employee_Name"] = org.employee_Name
        emporg["performance"] = org.performance
        
        return Response(emporg,status=status.HTTP_200_OK)

    def put(self,request,id,*args,**kwargs):
        org = self.get_queryset(id)

        branch = request.data["branch"]
        performance=request.data["performance"]

        org.branch=branch
        org.performance=performance
        org.save()

        change = {
            branch,
            performance
        }

        return Response('Details Updated',change, status=status.HTTP_200_OK)








