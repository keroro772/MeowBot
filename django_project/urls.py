from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^ZpX0Sea0wZy0EzUcH32m/', include(admin.site.urls)),
    url(r'^catnip/', include('Catnip.urls')),
    url(r'^ranks/', include('ranks.urls')),
    url(r'^Throwdown/', include('throwthursday.urls')),
    url(r'^drops/', include('Randomdrop.urls')),
    url(r'^goals/', include('goals.urls')),
    url(r'^accounts/', include('registration.backends.hmac.urls')),
    url(r'', include('social_django.urls')),
    url(r'^$', include('Home.urls')),
]
