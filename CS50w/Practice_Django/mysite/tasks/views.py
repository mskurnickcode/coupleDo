from django.shortcuts import render
from django import forms
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
class NewTaskForm(forms.Form):
    task=forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html", {
        "tasks": request.session["tasks"]
    })

# Add a new task:
def add(request):

    #check if POST
    if request.method == "POST":
        #Save form data in POST as form
        form = NewTaskForm(request.POST)

        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))

        else:
            #If form is invalid return the form to the form page
            return render(request, "tasks/add.html", {
            "form":form
            })


    else:
        return render(request, "tasks/add.html", {
            "form":NewTaskForm()
        })