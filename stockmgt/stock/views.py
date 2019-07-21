from django.shortcuts import render,redirect,get_object_or_404
# from .models import *
from .forms import *

# Create your views here.


def index(request):
    return render(request, 'index.html')


def display_switch(request):
    return render(request, 'display_switch.html')


def display_Ap(request):
    items = Ap.objects.all()
    context = {
        'items': items,
        'header': 'Access Points',

    }

    return render(request, 'index.html', context)


def display_PowerSupply(request):
    items = PowerSupply.objects.all()
    context = {
        'items': items,
        'header': 'Power Supplies',

    }

    return render(request, 'index.html', context)

def add_device(request, cls):
    if request.method =='POST':
        form = cls(request.POST)

    if form.is_valid():
        form.save()
        return redirect('index')

    else:
        form = SwitchForm()
        return render(request, 'add_new.html', {'form': form})



def add_switch(request):
    return add_device(request, SwitchForm)

def add_ap(request):
    return add_device(request, ApForm)


def add_power_supply(request):
    return add_device(request, PowerSupplyForm)

def edit_device(request, pk, model, cls):
 item = get_object_or_404(model, pk=pk)

 if request.method == 'POST':
     form = cls(request.POST, instance=item)
     if form.is_valid():
         form.save()
         return redirect('index')
 else:
     form = cls(instance=item)

     return render(request, 'edit_item.html', {form:form})


def edit_switch(request,pk):
    return edit_device(request, pk, Switch,SwitchForm)

def edit_ap(request,pk):
    return edit_device(request, pk, Ap,ApForm)

def edit_power_supply(request,pk):
    return edit_device(request, pk, PowerSupply,PowerSupplyForm)

def delete_switch(request,pk):
    Switch.objects.filter(id=pk).delete()

    items = Switch.objects.all()

    context = {

        'items':items
    }
    return render(request,'index.html', context)


def delete_ap(request,pk):
    Ap.objects.filter(id=pk).delete()

    items = Ap.objects.all()

    context = {

        'items':items
    }
    return render(request,'index.html', context)




def delete_power_supply(request,pk):
    PowerSupply.objects.filter(id=pk).delete()

    items = PowerSupply.objects.all()

    context = {

        'items':items
    }
    return render(request,'index.html', context)