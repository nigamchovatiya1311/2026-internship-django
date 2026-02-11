from django.contrib import admin
from .models import Employee,Course,Studenttable,Inventory

# Register your models here.

admin.site.register(Employee)
admin.site.register(Course)
admin.site.register(Studenttable)
admin.site.register(Inventory)