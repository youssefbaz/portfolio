from django.urls import path

from . import views

urlpatterns = [
    path('home.html', views.home),
    path('ds_project.html', views.ds_project),
    path('code_project.html', views.code_project),
    path('blog.html', views.blog),
    path('layout.html', views.layout),
    ]