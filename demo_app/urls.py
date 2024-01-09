from django.urls import path
from .views import *

urlpatterns = [
    path('login',login,name='login'),
    path('register_page',register_page,name='register_page'),
    path("Validation",Validation,name="Validation"),
    
]
