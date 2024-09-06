from django.shortcuts import render
from .models import *
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class StudentApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    #Basic Authentication
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    # Session Authentication
    # authentication_classes = [SessionAuthentication]
    # permission_classes = [IsAuthenticated]