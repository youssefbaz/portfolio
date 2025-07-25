"""
URL configuration for monsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from base import views
#from django.conf import settings
#from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("base/", include("base.urls")),
    path('',views.home, name='home'),
    path('ds_project.html',views.ds_project, name='ds_project'),
    path('code_project.html',views.code_project, name='code_project'),
    path('genai_project.html',views.genai_project, name='genai_project'),
    #path('blog.html',views.blog, name='blog'),
    #path('blog1.html',views.blog1, name='blog1'),
    path('layout.html', views.layout),
]# + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
