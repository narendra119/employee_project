from rest_framework import serializers

class EmployeeSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    emp_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    # gender = serializers.CharField(max_length=1)
    

