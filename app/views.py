from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def registration(request):
    ERFO=RegistrationForm()
    d={'ERFO':ERFO}

    if request.method=='POST':
        DRFO=RegistrationForm(request.POST)
        if DRFO.is_valid():
            return HttpResponse(str(DRFO.cleaned_data))
    return render(request,'registration.html',d)