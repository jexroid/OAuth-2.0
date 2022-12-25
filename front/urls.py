from django.urls import path , include
from . import views
from django.views.generic import TemplateView
from django.conf.urls import url
from django.contrib import admin
from .views import signup, pagelogin, pagelogout

urlpatterns = [
    path('',  views.my_game),
    path('sw.js', views.service_worker),
    url(r'^signup$', signup, name='signup'),
    url(r'^login', pagelogin, name='login'),
    url(r'^logout', pagelogout, name='logout'),
    path('sw.js', (TemplateView.as_view(
      template_name="browsepages/sw.js",
      content_type='application/javascript',)),
      name='serviceworker'),
]