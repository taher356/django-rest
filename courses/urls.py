from django.urls import path,re_path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='course_list'),
    re_path(r'^(?P<pk>\d+)/$', views.RetriveUpdateDestroyCourse.as_view(), name='course_detail'),
    re_path(r'^(?P<course_pk>\d+)/reviews/$', views.ListCreateReview.as_view(), name='review_list'),
    re_path(r'^(?P<course_pk>\d+)/reviews/(?P<pk>\d+)/$', views.RetriveUpdateDestroyReview.as_view(), name='revew_detail')
]
