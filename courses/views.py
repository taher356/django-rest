from django.shortcuts import get_object_or_404
#from django.shortcuts import render  because we dont need rendering in rest
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.decorators import action, permission_classes
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

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        else:
            if request.method == 'DELETE':
                return False    

class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (
        IsSuperUser,
        permissions.DjangoModelPermissions,
        )
    queryset = models.Course.objects.all()
    serializer_class = serializers.CourseSerializer

    @action(methods=['get'],detail=True)
    def reviews(self,request,pk=None):
        self.pagination_class.page_size = 1
        reviews = models.Review.objects.filter(course_id=pk)

        page = self.paginate_queryset(reviews)

        if page is not None:
            Serializer = serializers.ReviewSerializer(page, many=True)
            return self.get_paginated_response(Serializer.data)
        
        Serializer = serializers.ReviewSerializer(reviews, many=True)
        return Response(Serializer.data)


class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    viewsets.GenericViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.ReviewSerializer