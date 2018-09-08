from django.urls import path

from . import views

app_name = 'moisture'

urlpatterns = [
    path('', views.moisture_list, name='mc_list'),
    path('add/', views.MoistureCreate.as_view(), name='add'),
    path('<uuid:pk>/xml', views.download_xml, name='download_xml'),
    path('<uuid:pk>/edit/',views.MoistureUpdate.as_view(), name='edit'),
    path('<uuid:pk>/delete/', views.MoistureDelete.as_view(), name='delete'),
    path('data', views.excel_xml, name='get_xml'),
]