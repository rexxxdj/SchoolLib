from django.shortcuts import render
from django.http import HttpResponse

def student_dashboard(request, sid):
    return HttpResponse('<h1> Student DashBoard  %s</h1> ' %sid)

def student_profile(request, sid):
    return HttpResponse('<h1> Student Profile %s </h1>' %sid)

def student_class(request, sid):
    return HttpResponse('<h1> Student Class %s </h1>' %sid)
