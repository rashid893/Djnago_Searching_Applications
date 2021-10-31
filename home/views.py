from django.contrib.messages.constants import SUCCESS
from django.http import request
from django.shortcuts import render,HttpResponse

from home.models import Companyclass, Employclass
from django.contrib import messages

# Create your views here.
def index(request):
    return HttpResponse("success")
def home(request):
    return render(request,'home.html')
def employdata(request):
    if request.method =="POST":
        empid=request.POST['empid']
        name=request.POST['name']
        age=request.POST['age']
        phone=request.POST['phone']
        city=request.POST['city']
        employ=Employclass(empid=empid,name=name,age=age,phone=phone,city=city)
        employ.save()
        messages.add_message(request,messages.SUCCESS,'Your Form Successfully Submited!')
        #msg="your Fomr Successfully Submited"
    #return render(request,'employ.html',)

    return render(request,'employ.html')#{'msg':msg})#,
def company(request):
    if request.method =='POST':
        
        jobid=request.POST['jobid']
        jobprofile=request.POST['jobprofile']
        salary=request.POST['salary']
        employid=request.POST['employid']
        company=Companyclass(jobid=jobid,jobprofile=jobprofile,salary=salary,employid=employid)
        company.save()
        messages.add_message(request,messages.SUCCESS,'Your Form SuccessFully Submited')
        #messages.add_message(request,messages.SUCCESS,'Your Form Successfull Submited!')
      #  msg="your Fomr Successfully Submited"


    return render(request,'company.html')#{'msg':msg})
def searching_comp(request):
    return render(request,'searching_comp.html')
def searching_emp(request):
    return render(request,'searching_emp.html')
def empdata(request):
    data=request.POST['data']
    
        
    info=Employclass.objects.filter(empid__exact=data)
    return render(request,'searching_emp.html',{'info':info})
def compdata(request):
    data=request.POST['data']
    info=Companyclass.objects.filter(jobid__exact=data)
    return render(request,'searching_comp.html',{'info':info})

def viewEmpData(request):
    EmpData=Employclass.objects.all()
    count=Employclass.objects.count()
   # EmpData=Employclass.objects.all()[0:1:1]
    #EmpData=Employclass.objects.filter(age__=30)
    return render(request,'viewdata.html',{'EmpData':EmpData,'count':count})#age:age
def viewcompdata(request):
  
    count=Companyclass.objects.count()
    Empdata=Companyclass.objects.all()
    return render (request,'viewdata.html',{'Empdata':Empdata,'count':count})


