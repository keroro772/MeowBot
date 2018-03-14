from django.contrib import admin

from .models import Throw

def Viewer_Won(modelAdmin, request, queryset):
    for x in queryset:
        x.points += 3
        x.save()
    queryset.update(matchdone=True)
Viewer_Won.short_description = 'User won a match adds 3 points and sets matchdone'

def Viewer_Lost(modelAdmin, request, queryset):
    for x in queryset:
        x.points += 1
        x.save()
    queryset.update(matchdone=True)
Viewer_Lost.short_description = 'User Lost a match adds 1 point and sets matchdone'

def Viewer_Reset(modelAdmin, request, queryset):
    queryset.update(matchdone=False)
Viewer_Reset.short_description = 'resets matchdone of all selected'

class ThrowAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'points', 'matchdone')
    list_filter = ('matchdone','points')
    actions = [Viewer_Won, Viewer_Lost, Viewer_Reset]

admin.site.register(Throw, ThrowAdmin)