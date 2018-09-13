from django.urls import path

from . import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginFormView.as_view(), name='login'),
    path('logout/', views.LogoutFormView.as_view(), name='logout'),
]