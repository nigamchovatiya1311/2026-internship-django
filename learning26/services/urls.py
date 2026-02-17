from .import views
from django.urls import path


urlpatterns = [
    path('servicelist/', views.serviceList, name='service-list'),# name is used to refer url in html file
    path('createService/', views.createService, name='create-service'),
    path('deleteService/<int:id>/', views.deleteService, name='delete-service'), #<int:id> is used to pass id from url
    path('updateService/<int:id>/', views.updateService, name='update-service'), 


    #student activity urls only for learning purpose
    path('studentActivityList/', views.studentActivityList, name='student-activity-list'),
    path('createStudentActivity/', views.createStudentActivity, name='create-student-activity'),
    path('deleteStudentActivity/<int:id>/', views.deleteStudentActivity, name='delete-student-activity'),
    path('updateStudentActivity/<int:id>/', views.updateStudentActivity, name='update-student-activity'),
]