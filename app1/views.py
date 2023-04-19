from django.shortcuts import render,HttpResponse

# Create your views here.
def home(rquest):
    return HttpResponse('test git')