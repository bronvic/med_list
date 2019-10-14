from django.contrib import admin
from med_list.models import Drug, Description


class DrugAdmin(admin.ModelAdmin):
    pass


class DescriptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Drug, DrugAdmin)
admin.site.register(Description, DescriptionAdmin)