from django.conf.urls import url
from . import views
app_name = 'Goal_List'

urlpatterns = [
    url(r'^$', views.index, name='Goal'),
]
