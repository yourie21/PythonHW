from django.conf.urls import url, include #gives us access to function url
from . import views # to import the sibling VIEW file


urlpatterns = [
    url(r'^$', views.index),
    url(r'^process$', views.process),
    url(r'^result$', views.result), 
    url(r'^reset$', views.reset),
    # url(r'^(?P<number>\d+)$', views.show),
   
]