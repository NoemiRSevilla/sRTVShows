from django.conf.urls import url
from . import views
                    
urlpatterns = [
    url(r'^shows$', views.shows),
    url(r'^shows/new$', views.new),
    url(r'^shows/(?P<id>\d+)/edit$', views.edit),
    url(r'^shows/(?P<id>\d+)/destroy$', views.destroy),
    url(r'^shows/(?P<id>\d+)', views.infoonshow)
]