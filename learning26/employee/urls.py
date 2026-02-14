from . import views
from django.urls import path

urlpatterns = [
    path('employeeList/', views.employeeList, name='employeeList'),  #name is used to refer url in html file
    path('employeeFilter/', views.employeeFilter),
    path('createEmployee/', views.createEmployee),
    path('createEmployeeWithForm/', views.createEmployeeWithForm, name='createEmployee'), #name is used to refer url in html file
    path('createCourse/', views.createCourse),
    path('createStudent/', views.createStudent),
    path('createInventory/', views.createInventory),
    # path('deleteEmployee/', views.deleteEmployee, name='deleteEmployee'), #name is used to refer url in html file
    path('deleteEmployee/<int:id>/', views.deleteEmployee, name='deleteEmployee'), #name is used to refer url in html file
    path('filterEmployee/', views.filterEmployee, name='filterEmployee'), #name is used to refer url in html file
    path('sortedEmployee/<int:id>/', views.sortedEmployee, name='sortedEmployee'), #name is used to refer url in html file
    path('updateEmployee/<int:id>/', views.updateEmployee, name='updateEmployee'), #name is used to refer url in html file
]