# main/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('', views.home, name='home'),
	path('logout/', views.logout, name='logout'),
	path('register/', views.register, name='register'),
]