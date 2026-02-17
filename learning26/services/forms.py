from django import forms
from .models import Servicetable, StudentActivity


class ServiceForm(forms.ModelForm):
    class Meta:
        model = Servicetable
        fields = '__all__' #['name','description','price','duration']


# student activity form only for learning purpose
class StudentActivityForm(forms.ModelForm):
    class Meta:
        model = StudentActivity
        fields = '__all__'
