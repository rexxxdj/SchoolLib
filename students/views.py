from django.shortcuts import render, redirect
from django.http import HttpResponse

def student_index(request):
    return redirect('/student/1/dashboard')

def student_dashboard(request, sid):
    todayTimeTable = (
        {'id' : 1,
         'lessonName' : 'Англійська мова',
         'lessonStartTime' : '08:30',
         'lessonEndTime' : '09:15',
         'ended' : True,
         'ordered' : 1},
        {'id' : 2,
         'lessonName' : 'Фізкультура',
         'lessonStartTime' : '09:25',
         'lessonEndTime' : '10:10',
         'ended' : True,
         'ordered' : 2},
        {'id' : 3,
         'lessonName' : 'Математика',
         'lessonStartTime' : '10:30',
         'lessonEndTime' : '11:15',
         'ended' : False,
         'ordered' : 3},
        {'id' : 4,
         'lessonName' : 'Історія України',
         'lessonStartTime' : '11:45',
         'lessonEndTime' : '12:30',
         'ended' : False,
         'ordered' : 4},
        {'id' : 5,
         'lessonName' : 'Математика',
         'lessonStartTime' : '12:45',
         'lessonEndTime' : '13:30',
         'ended' : False,
         'ordered' : 5},
    )
    return render(request, 'studentDashboard.html', {'todayTimeTable' : todayTimeTable})

def student_profile(request, sid):
    return HttpResponse('<h1> Student Profile %s </h1>' %sid)

def student_class(request, sid):
    return HttpResponse('<h1> Student Class %s </h1>' %sid)


'''
def login(request):
    return render(request, 'login.html', {})
'''
