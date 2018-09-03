from django.urls import path

from atterberg import views

app_name = 'atterberg'

urlpatterns = [
    #path('', views.IndexView.as_view(), name='index'),
    path('', views.AtterbergList.as_view(), name='list'),
    path('atterberg/add/', views.AtterbergCreate.as_view(), name='add'),
    path('atterberg/<uuid:pk>/xml', views.download_xml, name='download_xml'),
    path('atterberg/<uuid:pk>/edit/',views.AtterbergUpdate.as_view(), name='edit'),
    path('atterberg/<uuid:pk>/delete/', views.AtterbergDelete.as_view(), name='delete'),
    path('atterberg/data', views.excel_xml, name='get_xml'),
]