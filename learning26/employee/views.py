from django.shortcuts import render
from .models import Employee

# Create your views here.

def employeeList(request):
    # employees = Employee.objects.all() #select * from employee
    employees = Employee.objects.all().values()
    # employees = Employee.objects.all().values_list()

    print(employees)
    return render(request, 'employee/employee_list.html', {'employees': employees})


def employeeFilter(request):
    employees = Employee.objects.filter(name = 'John').values()#select * from employee where name = 'John'
    #selet  from employee where post = "Developer"
    employee2 = Employee.objects.filter(post ="Developer").values()
    #select  from employee where name = "Hardik Patel" and post = "Developer"
    employee3 = Employee.objects.filter(name ="Hardik Patel",post ="Developer").values()
    
    #>23
    #select * from employee where age > 23
    employee4 = Employee.objects.filter(age__gt = 23).values()
    employee5 = Employee.objects.filter(age__gte = 23).values() # gte >=

    #<23
    #select * from employee where age < 23
    employee6 = Employee.objects.filter(age__lt = 23).values()
    employee7 = Employee.objects.filter(age__lte = 23).values() # <= lte

    #string queries
    employee8 = Employee.objects.filter(post__exact = "Developer").values() #case sensitive
    employee9 = Employee.objects.filter(post__iexact = "developer").values() # i -- case insensitive

    #contains
    # name contains "r" records will be fetched
    employee10 = Employee.objects.filter(name__contains = "r").values() #case sensitive
    employee11 = Employee.objects.filter(name__icontains = "K").values() #case insensitive

    #startswith endswith
    employee12 = Employee.objects.filter(name__startswith = "U").values() #case sensitive
    employee13 = Employee.objects.filter(name__endswith = "i").values() #case sensitive
    employee14 = Employee.objects.filter(name__istartswith = "n").values() #case insensitive
    employee15 = Employee.objects.filter(name__iendswith = "M").values() #case insensitive

    #in 
    #select * from employee where name in ("nigam","Hardik Patel")
    employee16 = Employee.objects.filter(name__in = ["nigam","Hardik Patel"]).values() 

    #range
    employee17 = Employee.objects.filter(salary__range = (30000,50000)).values() # salary between 30000 and 50000

    #order by
    employee18 = Employee.objects.all().order_by('age').values() # order by age in ascending order
    employee19 = Employee.objects.all().order_by('-age').values() # order by age in descending order

    employee20 = Employee.objects.all().order_by('-salary').values() # order by salary in ascending order

    print("Query 1",employees)
    print("Query 2",employee2)
    print("Query 3",employee3)
    print("Query 4",employee4)
    print("Query 5",employee5)
    print("Query 6",employee6)
    print("Query 7",employee7)
    print("Query 8",employee8)
    print("Query 9",employee9)
    print("Query 10",employee10)
    print("Query 11",employee11)
    print("Query 12",employee12)
    print("Query 13",employee13)
    print("Query 14",employee14)
    print("Query 15",employee15)
    print("Query 16",employee16)
    print("Query 17",employee17)
    print("Query 18",employee18)
    print("Query 19",employee19)
    print("Query 20",employee20)
    return render(request, 'employee/employee_filter.html', {'employees': employees})


