from django.shortcuts import render, HttpResponse, redirect
# from django.contrib import messages
from time import gmtime, strftime
from django.utils.crypto import get_random_string

def index(request):
    return render(request, "word/index.html")

def process(request):
    # first way of storing the session without restarting the log------
    log = []
    if "log" in request.session:
        log = request.session['log']

    # second way of storing the session--------
    # if "log" not in request.session:
    #     request.session['log'] = []
    # log = request.session["log"]

    # set up capitalization and font size key starts
    if "font" in request.POST:
        word = request.POST["word"].upper()
        font = "large"
    else: 
        word = request.POST["word"]
        font = "small"

    # set a default color of user didn't pick
    if "color" not in request.POST:
        color = "green"
    else: #this else is needed
        color = request.POST["color"]

    log.append({
        "word": word,
        "color": color,
        "font": font,
        "time":strftime ("%Y-%m-%d %H:%M %p")
    })
    request.session['log'] = log

    print(request.session["log"])
    return redirect("/word/result") #it redirect to the main, so start from 8000


def result(request):
    return redirect("/word") #this is home url ("/")


def reset(request):
    request.session.clear()
    print("You finally made it to RESETTTT!")
    return redirect("/word") #this is home url ("/")