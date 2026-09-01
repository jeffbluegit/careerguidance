from django.urls import path

from .views import dashboard_view, index_view, registration_view, students_view, addstudents_view

urlpatterns = [
    path('', index_view, name='index'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('registration/', registration_view, name='registration'),
    path('students/', students_view, name='students'),
    path('addstudents/', addstudents_view, name='addstudents'),
]
