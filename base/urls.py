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
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)