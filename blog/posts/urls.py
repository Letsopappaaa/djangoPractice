from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', post_list, name='list'),
    url(r'^create/$', post_create, name='create'),
    url(r'^(?P<id>\d+)/$', posts_detail, name='detail'),
    url(r'^categories/(?P<hashtag>[\w.@+-]+)/$', categories, name='categories'),

    #url(r'^$', post_delete, name='delete'),
    #url(r'^$', post_detail, name='detail'),
]
