from django.conf.urls import url
from . import views

app_name = 'codefortheyoung'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/$', views.index, name='index'),
	url(r'^about/$', views.about, name='about'),
	url(r'^join-us/$', views.join_us, name='join-us'),
	url(r'^join/$', views.join, name='join'),

]
