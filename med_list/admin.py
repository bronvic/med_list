from django.contrib import admin
from med_list.models import Drug, Description


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)
    search_fields = ['name', 'description__id']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    fields = ('id', 'description',)
    readonly_fields = ('id',)

    list_display = ('id', 'short_description',)
    search_fields = ['id']
