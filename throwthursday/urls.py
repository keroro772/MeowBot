from django.conf.urls import url
from . import views
app_name = 'Throwdown_List'

urlpatterns = [
    url(r'^$', views.index, name='Throwdown'),
    url(r'^signup/', views.sign_up, name='Signup'),
    url(r'^remove_me/', views.Remove_self, name='Removeme'),
]
