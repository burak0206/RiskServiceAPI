"""RiskServiceApi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RiskServiceApp import controller

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', controller.index),
    path('log', controller.log),
    path('risk/isuserknown', controller.is_user_known),
    path('risk/isclientknown', controller.is_client_known),
    path('risk/isipknown', controller.is_ip_known),
    path('risk/isipinternal', controller.is_ip_internal),
    path('risk/lastsuccessfullogindate', controller.get_last_successful_login_date),
    path('risk/lastfailedlogindate', controller.get_last_failed_login_date),
    path('risk/failedlogincountlastweek', controller.get_failed_login_count_lastweek),
]
