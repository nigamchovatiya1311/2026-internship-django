from django.urls import path
from . import views

urlpatterns = [
   path('home',views.studentHome),
   path('dashbord',views.studentDashbord),
   path('details',views.studentDetails),
   path('profile',views.studentProfile),
   path('archivement',views.studentArchivement),

   # crispy form for student services
   path('services',views.serviceList, name='service_list'),
   path('servicescreate',views.serviceCreate, name='service_create'),
   path('servicesdelete/<int:service_id>/', views.deleteService, name='delete_service'),
]