from django.db import models

# Create your models here.


class Student(models.Model):
    studentName = models.CharField(max_length=50)
    studentAge = models.IntegerField()
    studentCity = models.CharField(max_length=40)
    studentEmail = models.EmailField(null=True)

    #meta class
    class Meta:
        db_table = "student" #table name in database

    def __str__(self):
        return self.studentName          


class Product(models.Model):
    productName = models.CharField(max_length=50)
    productPrice = models.IntegerField()
    productDescription = models.TextField()
    productStock = models.PositiveIntegerField()
    productColor = models.CharField(max_length=20,null=True)
    productStatus = models.BooleanField(default=True)

    #meta class
    class Meta:
        db_table = "product" #table name in database    


class Car(models.Model):
    carName = models.CharField(max_length=50)
    carPrice = models.PositiveIntegerField()
    carCompany = models.CharField(max_length=40)

    #meta class
    class Meta:
        db_table = "car" #table name in database     


# One to One relationship

hobbies = (('cricket','Cricket'),('football','Football'),('badminton','Badminton'))
class StudentProfile(models.Model):
    # one to one relationship with student table
    studentId = models.OneToOneField(Student,on_delete=models.CASCADE)
    studentHobbies = models.CharField(max_length=20,choices=hobbies)
    studentAddress = models.TextField(max_length=100)
    studentPhone = models.CharField(max_length=10)
    studentGender = models.CharField(max_length=10)
    studentDOB = models.DateField()

    #meta class
    class Meta:
        db_table = "studentprofile" #table name in database

    def __str__(self):
        return self.studentId.studentName
    

# one to one relationship ex.

class Booking(models.Model):
    bookingId = models.AutoField(primary_key=True)
    bookingDate = models.DateField()
    bookingTime = models.TimeField()
    # one to one relationship with studentprofile table
    
    #meta class
    class Meta:
        db_table = "booking"

    def __str__(self):
        return str(self.bookingId)
    
class Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    paymentAmount = models.IntegerField()
    paymentDate = models.DateField()
    paymentTime = models.TimeField()
    # one to one relationship with booking table
    bookingId = models.OneToOneField(Booking,on_delete=models.CASCADE)

    #meta class
    class Meta:
        db_table = "payment"

    def __str__(self):
        return str(self.paymentId)    
        



# One to Many relationship
class Category(models.Model):
    categoryName = models.CharField(max_length=100)
    categoryDescription = models.TextField()
    categoryStatus = models.BooleanField(default=True)
    
    #meta class
    class Meta:
        db_table = "category"

    def __str__(self):
        return self.categoryName   


class Service(models.Model):
    serviceName = models.CharField(max_length=100)
    serviceDescription = models.TextField()
    servicePrice = models.IntegerField()
    serviceStatus = models.BooleanField(default=True)
    discount = models.IntegerField(null=True)
    #foreign key to connect one to many relationship category table
    categoryId = models.ForeignKey(Category,on_delete=models.CASCADE)

    #meta class
    class Meta:
        db_table = "service"

    def __str__(self):
        return self.serviceName   
    

# one to many relationship ex.

class Offer(models.Model):
    offerid = models.AutoField(primary_key=True)
    offerName = models.CharField(max_length=100)
    offerDescription = models.TextField()
    offerValidfrom = models.DateField()
    offerValidto = models.DateField()

    #meta class
    class Meta:
        db_table = "offer"

    def __str__(self):
        return str(self.offerid)
    
class BookingOrder(models.Model):
    orderId = models.AutoField(primary_key=True)
    orderDate = models.DateField()
    # foreign key to connect one to many relationship with offer table
    offerId = models.ForeignKey(Offer,on_delete=models.CASCADE)

    #meta class
    class Meta:
        db_table = "bookingorder"

    def __str__(self):
        return str(self.orderId)
    
 #ex--2 

class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    customerName = models.CharField(max_length=100)
    customerEmail = models.EmailField()
    customerPhone = models.CharField(max_length=10)

    #meta class
    class Meta:
        db_table = "customer"

    def __str__(self):
        return self.customerName  
    
class Purchase(models.Model):
    purchaseId = models.AutoField(primary_key=True)
    purchaseDate = models.DateField()
    purchaseAmount = models.FloatField()
    # foreign key to connect one to many relationship with customer table
    customerId = models.ForeignKey(Customer,on_delete=models.CASCADE)

    #meta class
    class Meta:
        db_table = "purchase"

    def __str__(self):
        return str(self.purchaseId)    



    

   







    
    
