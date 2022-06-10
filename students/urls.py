from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
    path(r'<int:sid>/dashboard', views.student_dashboard, name='student_dashboard'),
    path(r'<int:sid>/profile', views.student_profile, name='student_profile'),
    path(r'<int:sid>/class', views.student_class, name='student_class'),
]
