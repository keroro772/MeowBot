from django.conf.urls import url
from . import views
app_name = 'RandomDrops'

urlpatterns = [
    url(r'^$', views.index, name='RandomDrops'),
]
