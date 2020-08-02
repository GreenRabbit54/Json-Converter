from .models import Persons
from django.shortcuts import render

#default page
def index(request):
    people = Persons.objects.all()
    return render(request, 'index.html', {'people':people})

#sorting by employee

def employer(request):
    people1 = Persons.objects.all().order_by('employer')
    return render(request, 'employer.html', {'people1':people1})

#sorting by employersCount
def employeesCount(request):
    people = Persons.objects.all().order_by('-employeesCount')
    return render(request,'employeesCount.html', {'people':people})
