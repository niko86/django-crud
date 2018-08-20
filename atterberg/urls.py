from django.urls import path

from atterberg import views

app_name = 'atterberg'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('atterbergs', views.AtterbergList.as_view(), name='atterberg-list'),
    path('atterberg/add/', views.AtterbergCreate.as_view(), name='atterberg-add'),
    path('atterberg/<uuid:pk>/xml', views.download_xml, name='atterberg-xml'),
    path('atterberg/<uuid:pk>/edit/',views.AtterbergUpdate.as_view(), name='atterberg-edit'),
    path('atterberg/<uuid:pk>/delete/', views.AtterbergDelete.as_view(), name='atterberg-delete'),
]