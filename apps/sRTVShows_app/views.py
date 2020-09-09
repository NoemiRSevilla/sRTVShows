from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Shows

def new(request):
    if request.method == "GET":
        return render(request, "new.html")
    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect ("/shows/new")
        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            new_show = Shows.objects.create(title=request.POST['title'],
                                            network=request.POST['network'], release=request.POST['release'], description=request.POST['description'])
            messages.success(request, "Show successfully created")

            return redirect(f"/shows/{new_show.id}")


def shows(request):
    context = {
        "all_shows": Shows.objects.all()
    }
    return render(request, "shows.html", context)


def infoonshow(request, id):
    context = {
        "show": Shows.objects.get(id=id)
    }
    return render(request, "infoonshow.html", context)


def edit(request, id):
    if request.method == "GET":
        context = {
            "shows_info": Shows.objects.get(id=id)
        }
        return render(request, "edit.html", context)
    if request.method == "POST":
        errors = Shows.objects.basic_validator(request.POST)
        # check if the errors dictionary has anything in it
        if len(errors) > 0:
            shows_info = Shows.objects.get(id=id)
            # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
            for key, value in errors.items():
                messages.error(request, value)
            # redirect the user back to the form to fix the errors
            return redirect (f"/shows/{shows_info.id}/edit")
        else:
            # if the errors object is empty, that means there were no errors!
            # retrieve the blog to be updated, make the changes, and save
            shows_info = Shows.objects.get(id=id)
            title = request.POST['title']
            network = request.POST['network']
            release = request.POST['release']
            description = request.POST['description']
            shows_info.title = title
            shows_info.network = network
            shows_info.release = release
            shows_info.description = description
            shows_info.save()
            messages.success(request, "<div class='ohyes'>Show successfully updated</div>")
            return redirect(f"/shows/{shows_info.id}")


def destroy(request, id):
    showtodelete = Shows.objects.get(id=id)
    showtodelete.delete()
    return redirect("/shows")
