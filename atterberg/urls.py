from django.urls import path

from atterberg import views

app_name = 'att'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]