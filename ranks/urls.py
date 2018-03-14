from django.conf.urls import url
from . import views
app_name = 'Ranks'

urlpatterns = [
    url(r'^$', views.index, name='Ranks'),
]
