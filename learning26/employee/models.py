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
    
    
