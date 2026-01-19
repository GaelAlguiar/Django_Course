from django.shortcuts import render

# Create your views here.


def course_list(req):
    return render(req, "courses/courses.html")


def course_detail(req):
    pass


def course_lessons(req):
    pass
