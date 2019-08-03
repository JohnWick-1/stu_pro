
from .models import StudentPro
from rest_framework.serializers import ModelSerializer


class StudentProSerializer(ModelSerializer):
    class Meta:
        model = StudentPro
        fields ='__all__'   #['password']
