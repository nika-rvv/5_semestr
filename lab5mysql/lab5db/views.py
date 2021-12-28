from django.shortcuts import render

from lab5db.models import Faculty
from datetime import date

def facultyList(request):
    return render(request, 'faculties.html', {'data' : {
        'current_date': date.today(),
        'faculties': Faculty.objects.all()
    }})

def GetFaculty(request, id):
    return render(request, 'faculty.html', {'data' : {
        'current_date': date.today(),
        'faculty': Faculty.objects.filter(id=id)[0]
    }})
