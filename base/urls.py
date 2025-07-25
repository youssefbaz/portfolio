from django.urls import path

from . import views

urlpatterns = [
    path('home.html', views.home),
    path('ds_project.html', views.ds_project),
    path('code_project.html', views.code_project),
    path('genai_project.html', views.genai_project),
    #path('blog.html', views.blog),
    #path('blog1.html', views.blog1),
    path('layout.html', views.layout),
    ]