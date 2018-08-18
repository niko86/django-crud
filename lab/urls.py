from django.urls import path

from lab import views

app_name = 'lab'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('engineers', views.EngineerList.as_view(), name='engineer-list'),
    path('engineer/add/', views.EngineerCreate.as_view(), name='engineer-add'),
    path('engineer/<uuid:pk>/', views.EngineerDetail.as_view(), name='engineer-detail'),
    path('engineer/<uuid:pk>/edit/',views.EngineerUpdate.as_view(), name='engineer-edit'),
    path('engineer/<uuid:pk>/delete/', views.EngineerDelete.as_view(), name='engineer-delete'),
]
