from django.contrib import admin
from django.urls import path
from chatapp import views

urlpatterns = [
	path('', views.home_view, name='home'),
	path('course/', views.course_view, name='about'),
	path('admission/', views.admission_view, name='about'),
	path('about/', views.about_view, name='about'),
	path('contact/', views.contact_view, name='contact'),
	path('webhook/', views.webhook, name='webhook'),
]

