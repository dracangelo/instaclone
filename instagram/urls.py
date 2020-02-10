from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^login/$', views.login_user, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^search/$', views.search, name='search'),
    url(r'^signup_success/$', views.signup_success, name='signup_success'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^update_profile/$', views.update_profile, name='update_profile'),
    
    
    
]

# if settings.DEBUG:
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)