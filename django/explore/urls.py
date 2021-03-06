from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.search, name='search'),
    url(r'^view/', views.results, name='view'),
    url(r'^weight/', views.weight, name='weight'),
    url(r'^bargraphs/', views.bargraphs, name='bargraphs'),
    url(r'^details/', views.details, name = 'details'),
    url(r'^general/', views.general, name = 'general')
]
