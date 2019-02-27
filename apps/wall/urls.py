from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^registration$', views.registration_process),
    url(r'^login$', views.login_process),
    url(r'^wall$', views.wall),
    url(r'^post_message$', views.post_message),
    url(r'^post_comment$', views.post_comment),
    url(r'^log_off$', views.log_off),
]