from django.shortcuts import render,redirect,get_object_or_404
# from .models import *
from .forms import *

# Create your views here.


def index(request):

    import requests


    switches = requests.get("https://uccitstock.herokuapp.com/switch").json()
    accesspoints = requests.get("https://uccitstock.herokuapp.com/accesspoint").json()
    powersupplies = requests.get("https://uccitstock.herokuapp.com/powersupply").json()

    print(switches)

    response={"switches":switches,
              "accesspoints":accesspoints,
              "powersupplies":powersupplies}

    return render(request, 'index.html',{"response":response})


def display_switch(request):

    import requests

    switches = requests.get("https://uccitstock.herokuapp.com/switch").json()

    response = {"switches": switches}

    return render(request, 'display_switch.html', {"response": response})


def display_ap(request):

    import requests

    accesspoint = requests.get("https://uccitstock.herokuapp.com/accesspoints").json()

    response = {"accesspoint": accesspoint}

    return render(request, 'display_ap.html', {"response": response})


def display_powersupply(request):

    import requests

    powersupply = requests.get("https://uccitstock.herokuapp.com/powersupply").json()

    response = {"powersupply": powersupply}

    return render(request, 'display_powersupply.html', {"response": response})