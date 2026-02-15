from .import views
from django.urls import path


urlpatterns = [
    path('servicelist/', views.serviceList, name='service-list'),# name is used to refer url in html file
    path('createService/', views.createService, name='create-service'),
    path('deleteService/<int:id>/', views.deleteService, name='delete-service'), #<int:id> is used to pass id from url
    path('updateService/<int:id>/', views.updateService, name='update-service'), 
]