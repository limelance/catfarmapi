from django.contrib import admin
from .models import Cat


class CatAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'owner']

    class Meta:
        model = Cat

admin.site.register(Cat, CatAdmin)
