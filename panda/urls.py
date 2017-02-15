from django.conf.urls import url
from django.contrib import admin
from panda.pandapps import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.HomePage.as_view(), name='home'),
    url(r'^articles/$', views.ArticlesPage.as_view(), name='articles'),
    url(r'^detail-article/(?P<id>\d+)$', views.detail, name='detail-article'),
    url(r'^videos/$', views.VideosPage.as_view(), name='videos'),
    url(r'^contact/$', views.ContactPage.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
