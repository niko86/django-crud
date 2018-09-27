from django.urls import path

from . import views

app_name = 'lab'

urlpatterns = [
    path('', views.psd_list, name='list'),
    path('add/', views.PsdCreate.as_view(), name='add'),
    path('<uuid:pk>/xml', views.download_xml, name='download_xml'),
    path('<uuid:pk>/edit/',views.PsdUpdate.as_view(), name='edit'),
    path('<uuid:pk>/delete/', views.PsdDelete.as_view(), name='delete'),
    path('data', views.excel_xml, name='get_xml'),
]