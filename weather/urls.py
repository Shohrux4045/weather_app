from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('autocomplete/', views.autocomplete, name='autocomplete'),
    path('api/search-statistics/', views.search_statistics, name='search_statistics'),

]
