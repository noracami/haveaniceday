"""haveaniceday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from tables_of_month.views import home, table_list, table_detail
from order.views import order_list, order_detail

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^table/$', table_list, name='table_list'),
    url(r'^table/(?P<pk>\d+)/$', table_detail, name='table_detail'),
    url(r'^order/$', order_list, name='order_list'),
    url(r'^order/(?P<pk>\d+)/$', order_detail, name='order_detail'),
    url(r'^admin/', include(admin.site.urls)),
]
