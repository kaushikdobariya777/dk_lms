from django.conf.urls import url
from testapp import views

urlpatterns = [
    url('^$',views.greeting),
    url('about/',views.about),
    url('contact/',views.showContact),
    url('employee/',views.employee_info_view),
]
