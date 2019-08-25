from django.urls import path
from .import views

app_name = 'proto'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search/', views.SearchView.as_view(), name='search'),
    path('jaran/', views.jaran_search, name='jaran_search')
]
