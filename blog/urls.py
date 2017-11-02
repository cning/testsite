from django.conf.urls import url
from . import views

# any url like r'...', call views.bla and response.
urlpatterns = [
        url(r'^$', views.post_list, name='post_list'),
        # ?P<pk> take the followings as the value of variable pk
        # this pk is the argument of post_detail...
        url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]
