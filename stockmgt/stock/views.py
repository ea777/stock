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


def display_accesspoint(request):

    import requests

    accesspoint = requests.get("https://uccitstock.herokuapp.com/accesspoint").json()

    response = {"accesspoint": accesspoint}

    return render(request, 'display_ap.html', {"response": response})


def display_powersupply(request):

    import requests

    powersupply = requests.get("https://uccitstock.herokuapp.com/powersupply").json()

    response = {"powersupply": powersupply}

    return render(request, 'display_powersupply.html', {"response": response})

def edit_switch(request, id):

    import requests

    if request.method == "POST":

        print(request.POST.get('item_id', ''))
        print(request.POST.get('type', ''))
        print(request.POST.get('model', ''))
        print(request.POST.get('issues', ''))

        requests.put("https://uccitstock.herokuapp.com/update_switch/" + str(id)).json()
        return render(request, 'update_complete_switch.html')
    else:

        switch_details = (requests.put("https://uccitstock.herokuapp.com/switch/"+str(id)).json())

        response = {"switch_details": switch_details[0]}

        return render(request, 'edit_switch.html', {"response": response})

def edit_accesspoint(request, id):

 import requests

 accesspoint_details = (requests.get("https://uccitstock.herokuapp.com/accesspoint/"+str(id)).json())

 response = {"accesspoint_details": accesspoint_details[0]}

 return render(request, 'edit_accesspoint.html', {"response": response})


def edit_powersupply(request, id):

 import requests

 powersupply_details = (requests.get("https://uccitstock.herokuapp.com/powersupply/"+str(id)).json())

 response = {"powersupply_details": powersupply_details[0]}

 return render(request, 'edit_powersupply.html', {"response": response})




def delete_switch(request, id):

    import requests

    response = (requests.get("https://uccitstock.herokuapp.com/delete_switch/" + str(id)).json())

    print(response)

    return render(request, 'delete_switch_complete.html')


def delete_accesspoint(request, id):

    import requests

    response = (requests.get("https://uccitstock.herokuapp.com/delete_accesspoint/" + str(id)).json())

    print(response)

    return render(request, 'delete_accesspoint_complete.html')


def delete_powersupply(request, id):

    import requests

    response = (requests.get("https://uccitstock.herokuapp.com/delete_powersupply/" + str(id)).json())

    print(response)

    return render(request, 'delete_powersupply_complete.html')

def update_switch(request, id):

    import requests

