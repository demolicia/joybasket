
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact,name='contact'),
    path('Home/', views.index,name='home'),
    path('about/', views.about,name='about'),
]
