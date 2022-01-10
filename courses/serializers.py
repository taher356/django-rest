from django.db.models import fields
from rest_framework import serializers
from . import models

class ReviewSerializer(serializers.ModelSerializer):
    class meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        fields = (
            'id',
            'course',
            'name',
            'email',
            'comment',
            'review',
            'rating',
            'created_at'
        )
        model = models.Review

class CourseSerializer(serializers.ModelSerializer):
    class meta:
        fields = (
            'id',
            'title',
            'url'
        )
        model = models.Course        