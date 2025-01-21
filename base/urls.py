from base.views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'base'

urlpatterns = [
    path('users/', getUsers.as_view(), name='getUsers'),
    path('user/add/', addUser.as_view(), name='addUser'),
    path('user/<id>/', showUser.as_view(), name='showUser'),
    path('user/<id>/edit/', editUser.as_view(), name='editUser'),
    path('user/<id>/delete/', deleteUser.as_view(), name='deleteUser'),

    path('employees/', getEmployees.as_view(), name='getEmployees'),
    path('employee/add/', addEmployee.as_view(), name='addEmployee'),
    path('employee/<id>/', showEmployee.as_view(), name='showEmployee'),
    path('employee/<id>/edit/', editEmployee.as_view(), name='editEmployee'),
    path('employee/<id>/delete/', deleteEmployee.as_view(), name='deleteEmployee'),

    path('attendance/', getAttendances.as_view(), name='getAttendances'),
    path('attendance/add/', addAttendance.as_view(), name='addAttendance'),
    path('attendance/<id>/', showAttendance.as_view(), name='showAttendance'),
    path('attendance/<id>/edit/', editAttendance.as_view(), name='editAttendance'),
    path('attendance/<id>/delete/', deleteAttendance.as_view(), name='deleteAttendance'),
] 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
