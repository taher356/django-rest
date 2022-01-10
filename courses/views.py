#from django.shortcuts import render  because we dont need rendering in rest
from django.db.models.query import QuerySet
from rest_framework import generics

from . import models
from . import serializers

class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetriveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer
    
    