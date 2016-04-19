from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^all/$', views.order_list, name='order_list'),
    url(r'^(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
    url(r'^member/all/$', views.member_list, name='member_list'),
    url(r'^member/$', views.member_detail, name='member_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]
