from django.contrib import admin
from .models import Course,Review
# Register your models here.


class ReviewAdmin(admin.ModelAdmin):
    pass

admin.site.register(Review, ReviewAdmin)
admin.site.register(Course)