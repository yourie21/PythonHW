from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string
import random

def index(request):
    if "gold" not in request.session:
        request.session['gold'] = 0
        # request.session['log'] = []
    return render(request, "gold/gold.html")

def process(request):
    print (request.POST)
    if "list" not in request.session:
        request.session['list'] = []
    log = request.session['list']
    num = 0
    time = strftime(" %Y /%m /%d %H:%M") 

    if request.POST["location"] == "farm":
        num = random.randint(10,20)
        request.session['gold'] += num
        log.append({
            "color": "green",
            "log": f"you've earned {num} number of golds from farm!! (time: {time}) "
        })  
        request.session['list'] = log 

    elif request.POST["location"] == "cave":
        num = random.randint(5,10)
        request.session['gold'] += num
        log.append({
            "color": "blue",
            "log": f"you've earned {num} number of golds from cave!! (time: {time}) "
        })  
        request.session['list'] = log 

    elif request.POST["location"] == "house":
        num = random.randint(2,5)
        request.session['gold'] += num
        log.append({
            "color": "orange",
            "log": f"you've earned {num} number of golds from house!! (time: {time}) "
        })  
        request.session['list'] = log 

    elif request.POST["location"] == "casino":
        num = random.randint(-50,50)
        if num >= 0:
            request.session['gold'] += num        
            log.append({
                'color' : 'purple',
                'log': f"Earned {num} from the Casino. {time}"
            })
        else:
            request.session['gold'] += num       
            log.append({
                'color' : 'red',
                'log': f"Oh No!! LOST {num} from the Casino. {time}"
            })
        request.session['list'] = log
    return redirect("/gold")

def reset(request):
    request.session.clear()
    return redirect("/gold")
