from django.conf.urls import include, url
from django.contrib import admin
from tables_of_month import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    #url(r'^table/$', table_list, name='table_list'),
    url(r'^(?P<pk>\d+)/$', views.table_detail, name='table_detail'),
    #url(r'^admin/', include(admin.site.urls)),
]
