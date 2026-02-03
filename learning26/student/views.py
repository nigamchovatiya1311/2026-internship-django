from django.shortcuts import render

# Create your views here.
def studentHome(request):
    return render(request, 'student/home.html')

def studentDashbord(request):
    return render(request, 'student/dashbord.html')

def studentDetails(request):
    details = {"Boys": 120, "Girls":100, "Class10": 100, "Class12":120 }
    return render(request, 'student/details.html',details)

def studentProfile(request):
    student1 = {"name": "John Doe", "age": 20, "course": "Cs"}
    student2 = {"name": "Jane Smith", "age": 22, "course": "Me"}
    student3 = {"name": "Mike Johnson", "age": 21, "course": "Ec"}
    sdata = {"s1": student1, "s2": student2, "s3": student3}
    return render(request, 'student/profile.html', sdata)

def studentArchivement(request):
    archiv1 = {"beststudent2020": "John Doe"}
    archiv2 = {"beststudent2021": "Jane Smith"}
    total = {"a1": archiv1, "a2": archiv2}
    return render(request, 'student/archivement.html', total)