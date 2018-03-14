from django.contrib import admin

from .models import Clip

class clipAdmin(admin.ModelAdmin):
    list_display = ('id', 'game', 'name', 'link')
    list_filter = ('game',)
    
admin.site.register(Clip, clipAdmin)