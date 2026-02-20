from django.shortcuts import render,redirect
from .forms import Userform
from .models import User
from django.contrib.auth import login

# Create your views here.
 
def registerUser(request):

    if request.method == 'POST':
        form = Userform(request.POST or None) #or None is used to avoid error when form is empty
        if form.is_valid():
            #is_staff = true
            form.save()
            #auto login..
            # user = User.objects.get(username=form.cleaned_data['username'])
            # login(request,user)
            # return redirect('employeeList')
            return redirect('employeeList')
    else:
        form = Userform()
        return render(request,'core/register.html',{'form':form})