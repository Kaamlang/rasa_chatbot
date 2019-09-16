from django.contrib import admin
from django.urls import path, include

# from .views import home_view, course_view, admission_view, about_view, contact_view, webhook

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('chatapp.urls')),]

# urlpatterns += [
#     path('', home_view, name='home'),
#     path('course/', course_view, name='course'),
#     path('admission/', admission_view, name='admission'),
#     path('about/', about_view, name='about'),
#     path('contact/', contact_view, name='contact'),
#     path('webhook', webhook, name='webhook'),
# ]
