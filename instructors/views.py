from django.http import HttpResponse
from django.template import loader
from django.db.models import Q
from .models import Instructor, Language, Course
from django.shortcuts import render



def index(request):
    return HttpResponse(
        "Hello candidate!<br><br> Check the details for this test on <a href=https://github.com/leocosta-io/test-django-public>https://github.com/leocosta-io/test-django-public</a> or on the file README.md in your project."
    )


def list(request, language=None):
    template = loader.get_template("instructors/list.html")

    instructors = None

    ### Task 3: Get instructors from database and filter them based on the language
    instructors = Instructor.objects.all()

    if request.method == 'GET':
        if language:
            instructors = instructors.filter(languages__code=language)

    ### Task 3 - End

    context = {
        "instructors": instructors,
    }
    return HttpResponse(template.render(context, request))
