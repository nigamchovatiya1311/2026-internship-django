from django.contrib import admin
from .models import User, ServiceProvider, Customers, Services, Bookings, Payments, Invoice

# Register your models here.

admin.site.register(User)
admin.site.register(ServiceProvider)
admin.site.register(Customers)
admin.site.register(Services)
admin.site.register(Bookings)
admin.site.register(Payments)
admin.site.register(Invoice)
