from django.urls import path
from . import views
app_name = 'home'
urlpatterns = [
    path("", views.index, name="index"),
    path("profile/<str:email>", views.profile_page, name = "profile_page"),
    path("conference/<str:email>", views.conference_page, name="conference_page"),
    path("login", views.login_page, name="login_page"),
    path("signup", views.signup_page, name="signup_page"),

    
]