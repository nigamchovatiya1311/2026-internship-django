from django import forms
from .models import Servicetable


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicetable
        fields = '__all__' #['name','description','price','duration']
