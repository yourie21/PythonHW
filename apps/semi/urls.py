
from django.conf.urls import url, include #gives us access to function url
from . import views # to import the sibling VIEW file


urlpatterns = [
    url(r'^$', views.index),
    url(r'^new$', views.new),
    url(r'^create$', views.create),
    url(r'^(?P<user_id>\d+)$', views.show),
    url(r'^(?P<user_id>\d+)/edit$', views.edit),
    url(r'^update', views.update),
    url(r'^(?P<user_id>\d+)/destroy$', views.destroy)
]