from django.shortcuts import render,redirect
from sbadminapp.models import Customer

# Create your views here.
def index(request):
    return render(request,'index.html')
def insert(request):
    return render(request,'newcustomer.html')

def insert1(request):
    en=Customer(cname=request.POST.get('cname'),uemail=request.POST.get('email'),
    address=request.POST.get('address'),mobile=request.POST.get('mobile'))
    en.save()
    return redirect('/customer/listcust')
def listcust(request):
    cust=Customer.objects.all()
    return render(request,'listcustomers.html',{'cust':cust})
def dele(request,id):
    cust=Customer.objects.get(id=id)
    cust.delete()
    return redirect('/customer/listcust')
def edit(request,id):
    cust=Customer.objects.get(id=id)
    return render(request,'editcustomer.html',{'cust':cust})


def update(request,id):
    cust=Customer.objects.get(id=id)
    cust.cname=request.POST['cname']
    cust.address=request.POST['address']
    cust.email=request.POST['email']
    cust.mobile=request.POST['mobile']
    cust.save()
    return redirect('/customer/listcust')

def insertpro(request):
    return render(request,'newproduct.html')
