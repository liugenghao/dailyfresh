__Author__ = "Bill Lau"
from django.conf.urls import url
from df_user import views

urlpatterns = [
    url(r'^register/$', views.register),
    url(r'^register_handle/$', views.register_handle, name='register_handle'),
    url(r'^$', views.login),
    url(r'^login/', views.login, name='login'),
]
