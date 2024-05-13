from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)
@login_required
def profile(request):
    mystudentaccounts = Student.objects.filter(lastname=request.user.last_name, firstname=request.user.first_name)
    context={
        'mystudentaccounts' :mystudentaccounts,
    }

    return render(request, 'profile.html', context)

def home(request):
    context={

    }

    return render(request, 'home.html', context)
@user_passes_test(lambda u: u.groups.filter(name='teachers'))
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
@user_passes_test(lambda u: u.groups.filter(name='teachers'))
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
        #confirm message
        messages.success(request, "New Student Added Successfully!")

    else:
        form = StudentForm()
    #return the form and all of its fields in the place of context variables and lists
    return render(request, "studentform.html", \
        {"method": request.method, "form": form}
        
        )
@user_passes_test(lambda u: u.groups.filter(name='teachers'))
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
        #confirm message
        messages.success(request, "New Teacher Added Successfully!")
    else:
        form = TeacherForm()
    #return the form and all of its fields in the place of context variables and lists
    return render(request, "teacherform.html", \
        {"method": request.method, "form": form}
        
        )


def register(request):
    #if they are already on the page and submitting data
    form = RegistrationForm
    if request.method == 'POST':
        #collect all data from th eform and save it to "form" list
        form = RegistrationForm(request.post)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('')
        else: #they are viewing the form for the first time
            form = RegistrationForm()
    return render(request,"registration/registration.html",{'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

