from django.conf.urls import include, url
from django.contrib import admin
from order import views as order_views

urlpatterns = [
    url(r'^$', order_views.home, name='home'),
    url(r'^(?P<pk>\d+)/$', order_views.order_detail, name='order_detail'),
    url(r'^member/$', order_views.member_detail, name='member_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]
