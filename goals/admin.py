from django.contrib import admin

from .models import goals

class GoalsAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'total')

admin.site.register(goals, GoalsAdmin)