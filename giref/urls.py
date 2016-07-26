from django.conf.urls import url
from . import views

app_name = 'giref'
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^home/', views.index, name='index'),
	url(r'^about-us/', views.about_us, name='about-us'),
	url(r'^contact-us/', views.contact_us, name='contact-us'),
	url(r'^join-us/', views.join_us, name='join-us'),
]
