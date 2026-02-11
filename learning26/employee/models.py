from django.db import models

# Create your models here.

post = (('Manager','Manager'),('Developer','Developer'),('Designer','Designer'),('Tester','Tester'),('HR','HR'))
class Employee(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    salary = models.IntegerField()
    join_date = models.DateField()
    post = models.CharField(max_length=100, choices=post)

    #class meta
    class Meta:
        db_table = "employee"
        verbose_name_plural = "Employee"

    def __str__(self):
        return self.name
    

class Course(models.Model):
    name = models.CharField(max_length=100)
    duration = models.IntegerField()
    fees = models.IntegerField()

    class Meta:
        db_table = "course"
        verbose_name_plural = "Course"

    def __str__(self):
        return self.name
    
    
class Studenttable(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)

    class Meta:
        db_table = "studenttable"
        verbose_name_plural = "Studenttable"

    def __str__(self):
        return self.name
    

class Inventory(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        db_table = "inventory"
        verbose_name_plural = "Inventory"

    def __str__(self):
        return self.name  