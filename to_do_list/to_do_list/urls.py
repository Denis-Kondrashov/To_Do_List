from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.views.generic.edit import CreateView

from base.forms import MyUserCreationForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('auth/', include('django.contrib.auth.urls')),
    path('auth/registration',
         CreateView.as_view(
             template_name='registration/registration_form.html',
             form_class=MyUserCreationForm,
             success_url=reverse_lazy('base:tasks')
         ), name='registration',
         ),
]
