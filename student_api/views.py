from django.shortcuts import render

# Create your views here.
from .models import Students
from .serializers import StudentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# Create your views here.


@api_view(['GET'])
def index(request):
    
    if request.method == 'GET':
        students = Students.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
    else:
        return Response({'error':'Unexpected Error'})