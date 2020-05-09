from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.mail import send_mail, EmailMessage
from  .decorators import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required(login_url='login')
def dashboard(request):
    customers = Customer.objects.all()
    orders  = Orders.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status ='Pending').count()
    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'dashboard.html', context)

def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders_set.all()
    total_orders = orders.count()
    context = {'customer':customer, 'total_orders':total_orders, 'orders':orders}
    return render(request, 'customer.html',context)

@login_required(login_url='login')
def products(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request, 'products.html', context)

def UserRegistration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form':form})

@login_required(login_url='login')
def CreateOrder(request,pk):
    customer = Customer.objects.get(id=pk)
    ordercreate = OrderCreateForm(initial={'customer':customer})
    if request.method == 'POST':
        ordercreate = OrderCreateForm(request.POST)
        if ordercreate.is_valid():
            ordercreate.save()
            return redirect('dashboard')
    context = {'ordercreate':ordercreate}
    return render(request, 'order_create.html', context)

@login_required(login_url='login')
def UpdateOrder(request, pk):
    order = Orders.objects.get(id=pk)
    ordercreate = OrderCreateForm(instance=order)
    if request.method == 'POST':
        ordercreate = OrderCreateForm(request.POST, instance=order)
        if ordercreate.is_valid():
            ordercreate.save()
            return redirect('dashboard')
    context = {'ordercreate':ordercreate}
    return render(request, 'order_create.html', context)

@login_required(login_url='login')
def DeleteOrder(request, pk):
    order = Orders.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('dashboard')
    context = {'order_del':order}
    return render(request, 'order_delete.html', context)



