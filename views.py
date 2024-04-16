from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .forms import BookingForm

from .models import Departments,Doctors


def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def booking(request):
    form = BookingForm()
    dict_form={
        'form': form
    }
    return render(request, 'booking.html',dict_form)
def doctors(request):
    dict_docs={
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_docs)
def contact(request):
    return render(request, 'contact.html')

def department(request):
    dict_dept={
        'dept':Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)

