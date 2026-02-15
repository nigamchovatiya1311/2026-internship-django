from django.shortcuts import render,redirect
from .models import Servicetable
from .forms import ServiceForm

# Create your views here.

# one type of view(read) to display list of services
# read operation 
def serviceList(request):
    services = Servicetable.objects.all().values()
    return render(request, 'services/service_list.html', {'services': services})

# create view to create service
# create operation
def createService(request):
    print("Request Method:", request.method)
    if request.method == "POST":
        form = ServiceForm(request.POST)
        form.save() # it will save the form data to the database
        return redirect('service-list') # it will redirect to service list page after creating service
    else:
        #form object will be created with empty fields
        form = ServiceForm() # it will create an empty form
        return render(request, 'services/create_service.html', {'form': form})
    
# delete operation   

def deleteService(request, id):
    #delete from service where id = 1
    print("id from url:", id)
    Servicetable.objects.filter(id = id).delete() # delete service with given id
    #return HttpResponse("Service Deleted...")
    #service list redirect
    return redirect('service-list')

# update operation

def updateService(request, id):
    service = Servicetable.objects.get(id=id) # get service with given id
    if request.method == "POST":
        form = ServiceForm(request.POST, instance=service) # it will update the existing service with new data
        form.save() # it will save the form data to the database
        return redirect('service-list') # it will redirect to service list page after updating service
    else:
        form = ServiceForm(instance=service) # it will create a form with existing service data
        return render(request, 'services/update_service.html', {'form': form}) 