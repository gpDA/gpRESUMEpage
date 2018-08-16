from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
#NOT YET USED from django.contrib.auth.decorators import login_required


#from .forms import CustomUserCreationForm

def home(request):
    return render(request, 'home.html')

