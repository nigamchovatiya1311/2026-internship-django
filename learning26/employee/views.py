from django.shortcuts import render, HttpResponse
from .models import Employee
from .forms import EmployeeForm,CourseForm,StudentForm,InventoryForm

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


# mannually create employee record
def createEmployee(request):
    Employee.objects.create(name = "vaibhav", age = 20, email = "vaibhav@example.com", salary = 40000,join_date = "2024-01-01", post = "Developer")
    return HttpResponse("Employee Created...")


def createEmployeeWithForm(request):
    print("Request Method:", request.method)
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        form.save() # it will save the form data to the database
        return HttpResponse("Employee Created...")
    else:
        #form object will be created with empty fields
        form = EmployeeForm() # it will create an empty form
        return render(request, 'employee/create_employee.html', {'form': form})

def createCourse(request):
    if request.method == "POST":
        form = CourseForm(request.POST)
        form.save() # it will save the form data to the database
        return HttpResponse("Course Created...")
    else:
        #form object will be created with empty fields
        form = CourseForm() # it will create an empty form
        return render(request, 'employee/create_course.html', {'form': form})
    

def createStudent(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        form.save() # it will save the form data to the database
        return HttpResponse("Student Created...")
    else:
        #form object will be created with empty fields
        form = StudentForm() # it will create an empty form
        return render(request, 'employee/create_student.html', {'form': form})   

def createInventory(request):
    if request.method == "POST":
        form = InventoryForm(request.POST)
        form.save() # it will save the form data to the database
        return HttpResponse("Inventory Created...")
    else:
        #form object will be created with empty fields
        form = InventoryForm() # it will create an empty form
        return render(request, 'employee/create_inventory.html', {'form': form})     