from django.contrib import admin

from .models import Catnip

class CatnipAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'currentAmount')
    search_fields = ['name',]
    def get_ordering(self, request):
        return ['-amount']

admin.site.register(Catnip, CatnipAdmin)
