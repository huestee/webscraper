from django.urls import path
from scraper import views
#from .views import search_product, index

urlpatterns = [
    path('', views.index, name='index'),
    path('search', views.search, name='search'),
]
