from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from  .decorators import *


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required(login_url='login')
def dashboard(request):
    customers = Customer.objects.all()
    orders  = Orders.objects.all()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status ='Pending').count()
    context = {'customers':customers, 'orders':orders, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}
    return render(request, 'dashboard.html', context)

@login_required(login_url='login')
def customers(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.orders_set.all()
    total_orders = orders.count()
    context = {'customer':customer, 'total_orders':total_orders, 'orders':orders}
    return render(request, 'customer.html',context)

@login_required(login_url='login')
def products(request):
    add_product = AddProduct()
    if request.method == 'POST':
        add_product = AddProduct(request.POST)
        if add_product.is_valid():
            add_product.save()
            return redirect('products')

    products = Products.objects.all()
    context = {'products':products, 'add_product':add_product}
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

def UserProfile(request):
    if request.method == 'POST':
        u_form = UpdateUserForm(request.POST, instance=request.user)
        p_form = UpdateUserprofile_Form(request.POST, request.FILES, instance=request.user.customer)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile-page')
    else:
        u_form = UpdateUserForm(instance=request.user)
        p_form = UpdateUserprofile_Form(instance=request.user.customer)

    context = {'u_form':u_form, 'p_form':p_form}
    return render(request, 'accounts/profile.html', context)

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



