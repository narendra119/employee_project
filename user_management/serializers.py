from rest_framework import serializers

class OrganisationSerializer(serializers.Serializer):
    
    headQuarters = serializers.CharField(max_length=255)
    branch = serializers.CharField(max_length=255)


class EmployeeSerializer(serializers.Serializer):
    GENDER_CHOICES = (
        ('M', 'MALE'),
        ('F', 'FEMALE'),
        ('O', 'OTHER')
    )
    emp_id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField()
    organisation = OrganisationSerializer()
    dob = serializers.SerializerMethodField()
    # gender = serializers.CharField(max_length=1)
    
    def get_dob(self,obj):
        return obj.name + " " + obj.age
    

