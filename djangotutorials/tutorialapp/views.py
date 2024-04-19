from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)
def home(request):
    context={

    }

    return render(request, 'home.html', context)
def students(request):
    students = Student.objects.all() #gets all records and saves to a students list
    context={
        'students':students, #exports students list to the template(webpage)
    }

    return render(request, 'students.html', context)
def teachers(request):
    teachers = Teacher.objects.all()
    context={
        'teachers':teachers,
    }

    return render(request, 'teachers.html', context)

def studentform(request):
    context={}
    if request.method == "POST": #check for button click
        form = StudentForm(request.POST)
        if form.is_valid():
            context=""
            for name, value in form.cleaned_data.items():
                print("{}: ({}{}".format\
                    (name,type(value), value))
        #save data locally but not to the database yet
        requests = form.save(commit=False)

        #save each field to a local variable
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        middlename = form.cleaned_data['middlename']
        grade = form.cleaned_data['grade']
        requests.save()#save to the database
    else:
        form = StudentForm()
    #return the form and all of its fields in the place of context variables and lists
    return render(request, "studentform.html", \
        {"method": request.method, "form": form}
        
        )
def teacherform(request):
    context={}
    if request.method == "POST": #check for button click
        form = TeacherForm(request.POST)
        if form.is_valid():
            context=""
            for name, value in form.cleaned_data.items():
                print("{}: ({}{}".format\
                    (name,type(value), value))
        #save data locally but not to the database yet
        requests = form.save(commit=False)

        #save each field to a local variable
        firstname = form.cleaned_data['firstname']
        lastname = form.cleaned_data['lastname']
        roomnumber = form.cleaned_data['roomnumber']
        subject = form.cleaned_data['subject']
        requests.save()#save to the database
    else:
        form = TeacherForm()
    #return the form and all of its fields in the place of context variables and lists
    return render(request, "teacherform.html", \
        {"method": request.method, "form": form}
        
        )