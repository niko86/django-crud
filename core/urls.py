from django.urls import path, re_path
from django.views.generic.base import RedirectView

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^favicon.ico$', RedirectView.as_view(url='/staticfiles/favicon/favicon.ico')),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutFormView.as_view(), name='logout'),
]