from django.db import models

# Create your models here.

Role = (('customer','Customer'),('admin','Admin'),('Service Provider','Service Provider'))
Status = (('active','Active'),('inactive','Inactive'),('blocked','Blocked'))
class User(models.Model):
    userId = models.AutoField(primary_key=True)
    userFullName = models.CharField(max_length=100)
    userEmail = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    userPhone = models.CharField(max_length=10)
    userRole = models.CharField(max_length=20, choices=Role)
    userAddress = models.TextField(max_length=200)
    userCity = models.CharField(max_length=50)
    createdAt = models.DateTimeField(auto_now_add=True)
    userStatus = models.CharField(choices=Status)

    #meta class
    class Meta:
        db_table = "user"

    def __str__(self):
        return self.userFullName
    

approvalStatus = (('pending','Pending'),('approved','Approved'),('rejected','Rejected'))
class ServiceProvider(models.Model):
    providerId = models.AutoField(primary_key=True)
    user_Id = models.ForeignKey(User,on_delete=models.CASCADE)    
    garageName = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    opennigTime = models.TimeField()
    closingTime = models.TimeField()
    rating = models.FloatField()
    approvalStatus = models.CharField(choices=approvalStatus)

    #meta class
    class Meta:
        db_table = "serviceprovider"

    def __str__(self):
        return str(self.providerId) 
    

type = (('Car','Car'),('Bike','Bike'))
class Customers(models.Model):
    customerId = models.AutoField(primary_key=True)
    user_Id = models.ForeignKey(User,on_delete=models.CASCADE) 
    vehicleType = models.CharField()   
    vehicleNumber = models.CharField(max_length=20)
    vehicleModel = models.CharField(max_length=50)

    #meta class
    class Meta:
        db_table = "customers"

    def __str__(self):
        return str(self.customerId)    
    

class Services(models.Model):
    serviceId = models.AutoField(primary_key=True)
    providerId = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.FloatField()

    #meta class
    class Meta:
        db_table = "services"

    def __str__(self):
        return self.serviceName
    

bookingStatus = (('pending','Pending'),('completed','Completed'),('cancelled','Cancelled'))    
class Bookings(models.Model):
    bookingId = models.AutoField(primary_key=True)    
    customerId = models.ForeignKey(Customers,on_delete=models.CASCADE)
    providerId = models.ForeignKey(ServiceProvider,on_delete=models.CASCADE)
    serviceId = models.ForeignKey(Services,on_delete=models.CASCADE)    
    bookingDate = models.DateField()
    bookingStatus = models.CharField(choices=bookingStatus)

    #meta class
    class Meta:
        db_table = "bookings"
        
    def __str__(self):       
        return str(self.bookingId)     
    

paymentStatus = (('pending','Pending'),('completed','Completed'),('failed','Failed'))
class Payments(models.Model):
    paymentId = models.AutoField(primary_key=True)
    bookingId = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    amount = models.FloatField()
    paymentMethod = models.CharField(choices=(('cash','Cash'),('card','Card'),('online','Online')))
    paymentStatus = models.CharField(choices=paymentStatus)
    paymentDate = models.DateTimeField()

    #meta class
    class Meta:
        db_table = "payments"

    def __str__(self):
        return str(self.paymentId)     
    

class Invoice(models.Model):
    invoiceId = models.AutoField(primary_key=True)
    bookingId = models.ForeignKey(Bookings,on_delete=models.CASCADE)
    invoiceNumber = models.CharField(max_length=20)
    invoiceDate = models.DateField()
    totalAmount = models.FloatField()
    
    #meta class
    class Meta:
        db_table = "invoice"

    def __str__(self):
        return self.invoiceNumber    
