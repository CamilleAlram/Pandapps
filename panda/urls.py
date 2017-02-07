from django.conf.urls import url
from django.contrib import admin
from panda.pandapps import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
    url(r'^videos/$', views.VideosPage.as_view(), name='videos'),
]
