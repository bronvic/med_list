from django import forms
from django.contrib import admin

from med_list.models import Drug, Description


class DrugForm(forms.ModelForm):
    analogs = forms.ModelMultipleChoiceField(queryset=Drug.objects.all(), required=False, disabled=True)

    def __init__(self, *args, **kwargs):
        self.base_fields['analogs'].queryset = Drug.objects.filter(description_id=kwargs['instance'].description_id).exclude(pk=kwargs['instance'].id)

        super().__init__(*args, **kwargs)


@admin.register(Drug)
class DrugAdmin(admin.ModelAdmin):

    form = DrugForm

    list_display = ('names', 'description')
    search_fields = ['names', 'description__id']


@admin.register(Description)
class DescriptionAdmin(admin.ModelAdmin):
    fields = ('id', 'description',)
    readonly_fields = ('id',)

    list_display = ('id', 'short_description',)
    search_fields = ['id']
