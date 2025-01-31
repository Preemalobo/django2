from django.forms import ModelForm

from myapp.models import Items

class ItemsForm(ModelForm):
    class Meta:
        model = Items
        fields = ["name","quantity","price","description"]