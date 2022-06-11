from django.shortcuts import render, redirect
from django.http import HttpResponse

def student_index(request):
    return redirect('/student/1/dashboard')

def student_dashboard(request, sid):
    return HttpResponse('<h1> Student DashBoard  %s</h1> ' %sid)

def student_profile(request, sid):
    return HttpResponse('<h1> Student Profile %s </h1>' %sid)

def student_class(request, sid):
    return HttpResponse('<h1> Student Class %s </h1>' %sid)
