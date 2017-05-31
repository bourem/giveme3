from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/([0-9]*)/$', views.item_detail),
]
