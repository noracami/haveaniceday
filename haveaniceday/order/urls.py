from django.conf.urls import include, url
from django.contrib import admin
from order import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^(?P<pk>\d+)/$', views.order_detail, name='order_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]
