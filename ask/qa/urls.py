from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.q_new, name='q_new'),
    url(r'^login/$', views.logining, name='logining'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^ask/$', views.q_add, name='q_add'),
    url(r'^popular/$', views.q_popular, name='q_popular'),
    url(r'^new/$', views.test, name='test'),
    url(r'^question/(?P<id>\d+)/$', views.q_details, name='q_details'),
]
