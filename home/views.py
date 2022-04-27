from crypt import methods
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render

from .models import Users, conference, submissions

class signupForm(forms.Form):
    name = forms.CharField(label = "name")
    email = forms.CharField(label = "email")
    organisation = forms.CharField(label = "organisation")
    password = forms.CharField(label = "password")
    account_type = forms.CharField(label = "account_type")

class loginForm(forms.Form):
    email = forms.CharField(label = "email")
    password = forms.CharField(label = "password")


class conferenceForm(forms.Form):
    conference_name = forms.CharField(label = "conference_name")
    host_name = forms.CharField(label = "host_name")
    start_date = forms.CharField(label = "start_date")
    end_date = forms.CharField(label = "end_date")

class submissionsForm(forms.Form):
    submitter_name = forms.CharField(label="submitter_name")
    conference_name = forms.CharField(label="conference_name")
    title = forms.CharField(label="title")
    file = forms.FileField()


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
            account_type_i = form.cleaned_data["account_type"]

            Users.objects.create(name = name_i, email = email_i, organisation = organisation_i, password = password_i, account_type = account_type_i)

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
    message = ""
    if request.method == 'POST':
        form = submissionsForm(request.POST, request.FILES)
        if form.is_valid():
            message = "document uploaded successfuly"
            submitter_email_i = email_i
            conference_name_i = form.cleaned_data["conference_name"]
            document_i = form.cleaned_data["file"]
            print(submitter_email_i)
            submissions.objects.create(submitter_email = submitter_email_i , conference_name = conference_name_i, document = document_i)
        else:
            message = "document NOT uploaded successfully"

    return render(request, "home/profile.html", {
        "name": Users.objects.filter(email = email_i).first().name,
        "email" : email_i,
        "organisation" : Users.objects.filter(email = email_i).first().organisation,
        "account_type" : Users.objects.filter(email = email_i).first().account_type,
        "con_form" : conferenceForm(),
        "cons" : conference.objects.all(),
        "message": message
    })

def conference_page(request, email):
    email_i = str(email)

    if request.method == "POST":
        form = conferenceForm(request.POST)

        if form.is_valid():
            conference_name_i = form.cleaned_data["conference_name"]
            host_name_i = form.cleaned_data["host_name"]
            start_date_i = form.cleaned_data["start_date"]
            end_date_i = form.cleaned_data["end_date"]

            conference.objects.create(con_name = conference_name_i, host_organisation = host_name_i, start_date = start_date_i, end_date = end_date_i)
            email_i = "NULL"
    
    
    return render(request, "home/conference.html", {
        "cons" : conference.objects.all(),
        "email" : email_i,
        "sub_form" : submissionsForm()
    })

    
def submissions_page(request, email):
    email_i = str(email)

    return render(request, "home/submissions.html", {
        "subs" : submissions.objects.filter(submitter_email = email_i).all()
    })

