from django.shortcuts import get_object_or_404
#from django.shortcuts import render  because we dont need rendering in rest
from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


from . import models
from . import serializers


class ListCreateCourse(generics.ListCreateAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

class RetriveUpdateDestroyCourse(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer




class ListCreateReview(generics.ListCreateAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer
    
    def get_queryset(self):
        return self.queryset.filter(course_id=self.kwargs.get('course_pk'))  
    def perform_create(self, serializer):
        course = get_object_or_404(models.Course,pk=self.kwargs.get('course_pk'))
        serializer.save(course=course)
          

class RetriveUpdateDestroyReview(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(),course_id=self.kwargs.get('course_pk'),pk=self.kwargs.get('pk'))



class CourseViewSet(viewsets.ModelViewSet):
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    @action(methods=['get'],detail=True)
    def reviews(self,request,pk=None):
        course = self.get_object()
        Serializer = serializers.ReviewSerializer(course.reviews.all(), many=True)
        return Response(Serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer