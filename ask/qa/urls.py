from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.q_new, name='q_new'),
    url(r'^login/$', views.test, name='test'),
    url(r'^signup/$', views.test, name='test'),
    url(r'^ask/$', views.q_add, name='q_add'),
    url(r'^popular/$', views.q_popular, name='q_popular'),
    url(r'^new/$', views.test, name='test'),
    url(r'^question/(?P<id>\d+)/$', views.q_details, name='q_details'),
]
