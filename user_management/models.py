from django.db import models

# Create your models here.
# We create and access models through django orm
# Django ORM 

class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    
    emp_id = models.IntegerField(blank=False, unique=True)
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    def __str__(self):
        return self.name

<<<<<<< HEAD
class Organisation(models.Model):
    headQuarters=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    branch_Address=models.TextField(max_length=50)
    employee_ID=models.IntegerField(null=True)
    employee_Name=models.CharField(max_length=20,null=True)
    performance=models.CharField(max_length=40,null=True)
 
class Employee_Details(models.Model):
    Organisation=models.ForeignKey(Organisation,on_delete=models.CASCADE)
class Meta:
    order_with_respect_to='Organisation'
    def __str__ (self):
        return self.employee_Name
=======
class City(models.Model):
 
    name=models.CharField(max_length=100)
    metro=models.BooleanField()
    population=models.IntegerField()
    engieering_colleges_count=models.IntegerField()

    def __str__(self):
        return self.engieering_colleges_count
>>>>>>> 2c84930ea6d526e527591f905f1ea9186996133f
