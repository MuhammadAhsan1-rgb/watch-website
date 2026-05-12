from django.shortcuts import render
from model.models import watchesdata1
def homepage(request):
    return render(request , "homepage.html")

def service(request):
    return render(request , "services.html")

def watchespage(request):
    data = watchesdata1.objects.all()
    dataobj = {
        'data' : data
    } 
    
    return render(request , "watches.html" , dataobj)
  
    