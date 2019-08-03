from django.shortcuts import render
from .serializers import StudentProSerializer
from .models import StudentPro
from rest_framework.viewsets import ModelViewSet
from django.http import HttpResponse
# Create your views here.

class StudentViewSet(ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = StudentProSerializer
    queryset = StudentPro.objects.all()
    # print(queryset)
    # print(queryset.__dict__)
    # print(type(queryset))


from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def check(request):
    print('inside out')
    data=request.POST
    print(data)
    print("*"*30)
    return HttpResponse('<h1>inside post {{code}}</h1>')

