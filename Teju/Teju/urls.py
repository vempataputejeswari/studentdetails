"""Teju URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from studentdata import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("class/",views.ClassApiView.as_view()),
    path("class/<int:pk>",views.Classtable.as_view()),
    path("student/",views.StudentApiView.as_view()),
    path("student/<int:pk>",views.StudentDetail.as_view()),
    path("student/class/",views.StudentDetailByClass.as_view()),

]