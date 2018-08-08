from django.urls import path

from lab.views import AnotherView, IndexView

app_name = 'lab'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('another', AnotherView.as_view(), name='another'),
    #path('<int:question_id>/', views.detail, name='detail'),
    #path('<int:question_id>/results/', views.results, name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
