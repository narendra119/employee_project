from django.db import models

# Create your models here.
# We create and access models through django orm
# Django ORM 

class Organisation(models.Model):
    headQuarters=models.CharField(max_length=50)
    branch=models.CharField(max_length=20)
    branch_Address=models.TextField(max_length=50)
    employee_ID=models.IntegerField(null=True)
    employee_Name=models.CharField(max_length=20,null=True)
    performance=models.CharField(max_length=40,null=True)

    class Meta:
        ordering = ["branch"]
        
    def __str__(self):
        return self.headQuarters

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
    organisation=models.ForeignKey(Organisation,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.name



