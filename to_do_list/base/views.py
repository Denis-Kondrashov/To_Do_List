from django.shortcuts import render
from django.http import HttpResponse

def Taskslist(request):
    return HttpResponse('To Do List')
