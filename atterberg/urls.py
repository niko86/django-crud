from django.urls import path

from . import views

app_name = 'atterberg'

urlpatterns = [
    path('', views.att_list, name='att_list'),
    path('add/', views.AtterbergCreate.as_view(), name='add'),
    path('<uuid:pk>/xml', views.download_xml, name='download_xml'),
    path('<uuid:pk>/edit/',views.AtterbergUpdate.as_view(), name='edit'),
    path('<uuid:pk>/delete/', views.AtterbergDelete.as_view(), name='delete'),
    path('data', views.excel_xml, name='get_xml'),
]