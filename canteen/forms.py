from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.contrib.admin import widgets

from .models import products

class PostProduct(forms.ModelForm):

    class Meta:
        model = products
        fields = ('name', 'weight', 'cost', 'created_date',)
        labels = {
            'name': ('Название'),
            'weight': ('Количество'),
            'cost': ('Цена'),
            'created_date': ('Дата'),

        }

class select_date(forms.Form):
    my_field = forms.DateField(widget = forms.SelectDateWidget())