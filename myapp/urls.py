
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact),
    path('Home/', views.index),
    path('about/', views.about),
]
