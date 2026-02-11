from django import forms
from .models import Employee,Course,Studenttable,Inventory

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__' #['name','age','email','salary','join_date','post']

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'    


class StudentForm(forms.ModelForm):
    class Meta:
        model = Studenttable
        fields = '__all__'  

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = '__all__'                  