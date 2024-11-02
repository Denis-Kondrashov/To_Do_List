from django.urls import path

from . import views

urlpatterns = [
    path('', views.Taskslist, name='tasks')
]
