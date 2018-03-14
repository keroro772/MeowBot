from django.conf.urls import url
from . import views
app_name = 'Catnip_List'

urlpatterns = [
    url(r'^$', views.index, name='Catnip'),
]
