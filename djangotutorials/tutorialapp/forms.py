from django import forms
from .models import *

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname', 'lastname', 'middlename', 'grade']
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['firstname', 'lastname', 'roomnumber', 'subject']