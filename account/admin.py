from django.contrib import admin
from .models import User
from .models import Course


# Register your models here.
admin.site.register(User)

# admin.py
# from django.contrib import admin
# admin.py


class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'instructor', 'description')
    search_fields = ('title', 'instructor__username')

admin.site.register(Course, CourseAdmin)


# admin.site.register(Course)
