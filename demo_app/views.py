from django.shortcuts import render,redirect
from .models import *

Login_Page_link="validation/login_page.html"
register_page_link="validation/register_page.html"
# Create your views here.
def login(request):
    return render(request,Login_Page_link)

#registration page
def register_page(request):
    return render(request,register_page_link)

def Validation(request):
    return render(request,register_page_link)
