from django.shortcuts import render
from django.http import HttpResponse
from app.models import Employee

def first(request):
    return HttpResponse(" Wellcome to First website")
def second(request):
    return render(request,'second.html')
def third(request):
    return render(request,'third.html')
def four(request):
    return render(request,'four.html')  
def five(request):
    return render(request,'five.html')
def six(request):
    if request.method=='POST':
        employee=Employee()
        employee.name=request.POST.get('Name')
        employee.Email_id=request.POST.get('Email-id')
        employee.Role=request.POST.get('Role')
        employee.mobile_no=request.POST.get('mobile-no')
        employee.save()
    return render(request,'six.html')      

