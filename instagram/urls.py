from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^signup/$', views.signup, name='signup'),
]

