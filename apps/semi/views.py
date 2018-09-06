from django.shortcuts import render, redirect
from .models import User

def index(request):
    print(User.objects.all())
    context = {
        "all_users": User.objects.all()
    }
    return render (request, "index.html", context)

def new(request):
    return render(request, "new.html")

def create(request):
    newuser = User.objects.create(
        first = request.POST["first"],
        last = request.POST["last"],
        email = request.POST["email"]
    )
    return redirect(f"/users/{newuser.id}")

def show(request, user_id): #this is for the url users/(?P<user_id>)
    #query data base!!
    context ={
        "suser": User.objects.get(id=user_id),
    }
    # suser (show_user) is a dict of one row (like user in all_users), and suser.key will return the value 
    return render(request, "show.html", context)


def edit(request, user_id): #this is for the url users/(?P<user_id>)
    #query data base!!
    context ={
        "euser": User.objects.get(id=user_id),
    }
    return render(request, "edit.html", context)

def update(request):
    # ["user_id"]here is transfered from {{euser.id}} from edit above, bc that was used for name:val in html
    user = User.objects.get(id=request.POST["user_id"])
    #reassigning the first, last.. of User's row
    user.first = request.POST["first"]
    user.last = request.POST["last"] 
    user.email = request.POST["email"]
    user.save()
    return redirect("/users")

def destroy(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect("/users")