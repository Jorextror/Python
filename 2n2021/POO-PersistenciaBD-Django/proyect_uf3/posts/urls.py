from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:post_id>/vote/', views.vote, name='vote'),
    path('results', views.ResultsView.as_view(), name='results'),

]