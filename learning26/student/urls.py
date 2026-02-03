from django.urls import path
from . import views

urlpatterns = [
   path('home',views.studentHome),
   path('dashbord',views.studentDashbord),
   path('details',views.studentDetails),
   path('profile',views.studentProfile),
   path('archivement',views.studentArchivement),
]