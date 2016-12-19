from django.conf.urls import url
from django.contrib import admin
from pandapps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
]
