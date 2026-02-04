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
