from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# Create your views here.
def home(request):
        return render(request,'base/home.html')
def ds_project(request):
        return render(request,'base/ds_project.html')
def code_project(request):
        return render(request,'base/code_project.html')
def genai_project(request):
        return render(request,'base/genai_project.html')
#def blog(request):
#        return render(request,'base/blog.html')
#def blog1(request):
#        return render(request,'base/blog1.html')
def layout(request):
        return render(request,'base/layout.html')