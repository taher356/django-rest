from django.urls import path,re_path
from . import views

app_name = 'courses'
urlpatterns = [
    path('', views.ListCreateCourse.as_view(), name='course_list'),
    re_path(r'^(?P<pk>\d+)/$',views.RetriveUpdateDestroyCourse.as_view(), name='course_detail'),
]
