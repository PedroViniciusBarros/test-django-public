from django.contrib import admin
from .models import Instructor, Language, Course

admin.site.register(Instructor)
admin.site.register(Language)

#### Task 1.1: (Not required but nice to have) Add Course Model on Django Admin


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'sku', 'page')



admin.site.register(Course, CourseAdmin)


### Task 1.1 - End
