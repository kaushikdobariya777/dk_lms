"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
#from testapp import views as testapp_views
#from exam import views as exam_views
from django.urls import include
from django.conf.urls import url

urlpatterns = [
    url('testapp/',include('testapp.urls')),
    url('exam/',include('exam.urls')),
    url('BRMapp/',include('BRMapp.urls')),
    # url('^$',testapp_views.greeting),
    #path('about/',testapp_views.about),
    #path('contact/',testapp_views.showContact),
    #path('test/',exam_views.showTest),
    #path('result/',exam_views.showResult),
    path('admin/', admin.site.urls),
]
