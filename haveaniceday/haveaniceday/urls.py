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
from website_component import views as basic_views

urlpatterns = [
    url(r'^$', basic_views.home, name='home'),
    url(r'^table/', include('tables_of_month.urls', namespace="tables_of_month")),
    url(r'^order/', include('order.urls', namespace="order")),
    url(r'^admin/', include(admin.site.urls)),
]
