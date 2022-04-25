from crypt import methods
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Users

class signupForm(forms.Form):
    name = forms.CharField(label = "name")
    email = forms.CharField(label = "email")
    organisation = forms.CharField(label = "organisation")
    password = forms.CharField(label = "password")

class loginForm(forms.Form):
    email = forms.CharField(label = "email")
    password = forms.CharField(label = "passoword")

# Create your views here.
def index(request):
    return render(request, "home/index.html")

def login_page(request):

    if request.method == "POST":
        form = loginForm(request.POST)

        if form.is_valid():
            email_i = form.cleaned_data["email"]
            password_i = form.cleaned_data["password"]

            obj = Users.objects.filter(email = email_i)
            
            if not obj:
                return render(request, "home/login.html", {
                    "form" : loginForm(),
                    "message" : "Wrong Credentials"
                })
            
            elif obj.first().password != password_i:
                return render(request, "home/login.html", {
                    "form" : loginForm(),
                    "message" : "Passwords did not match"
                })
            else:
                return HttpResponseRedirect("profile/" + obj.first().email)
    return render(request, "home/login.html", {
        "form" : loginForm(),
        "message" : ""
    })

def signup_page(request):

    if request.method == "POST":
        form = signupForm(request.POST)

        if form.is_valid():
            name_i = form.cleaned_data["name"]
            email_i = form.cleaned_data["email"]
            organisation_i = form.cleaned_data["organisation"]
            password_i = form.cleaned_data["password"]

            Users.objects.create(name = name_i, email = email_i, organisation = organisation_i, password = password_i)

            return HttpResponseRedirect(reverse("home:login_page"))

        else:
            return render(request, "home/signup.html", {
                "form" : signupForm()
            })



    return render(request, "home/signup.html", {
        "form" : signupForm()
    })


def profile_page(request, email):
    email_i = str(email)
    return render(request, "home/profile.html", {
        "name": Users.objects.filter(email = email_i).first().name,
        "email" : email_i,
        "organisation" : Users.objects.filter(email = email_i).first().organisation
    })

