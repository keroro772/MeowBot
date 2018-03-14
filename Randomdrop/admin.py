from django.contrib import admin

from .models import RandomDrops

class RandomDropAdmin(admin.ModelAdmin):
    list_display = ('Name', 'type', 'price')
    def get_ordering(self, request):
        return ['Name']

admin.site.register(RandomDrops, RandomDropAdmin)