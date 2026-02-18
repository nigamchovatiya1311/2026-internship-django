from django.urls import path
from . import views

urlpatterns = [
   path('home',views.studentHome),
   path('dashbord',views.studentDashbord),
   path('details',views.studentDetails),
   path('profile',views.studentProfile),
   path('archivement',views.studentArchivement),
   path('services',views.serviceList, name='service_list'),
   path('servicescreate',views.serviceCreate, name='service_create'),
   path('servicesdelete/<int:service_id>/', views.deleteService, name='delete_service'),
]