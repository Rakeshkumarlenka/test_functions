from django.shortcuts import render
from CMS_app.models import Employee_model

# Create your views here.
def showemp(request):
    showall = Employee_model.objects.all()
    return render (request,'index.html',{"data":showall})