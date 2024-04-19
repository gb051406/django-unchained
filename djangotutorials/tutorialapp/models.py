from django.db import models

# Create your models here.
class Student(models.Model):

    GRADES =(
        ('9', '9'),
        ('10', '10'),
        ('11', '11'),
        ('12', '12'),
    )

    firstname = models.CharField(max_length=200, null=True, verbose_name="First Name ")
    lastname = models.CharField(max_length=200, null=True, verbose_name="Last Name ")
    middlename = models.CharField(max_length=200, null=True, verbose_name="Middle Name ")
    grade = models.CharField(max_length=200, null=True, choices=GRADES, verbose_name="Grade ")

    def __str__(self):
        return str(self.lastname) + ", " + str(self.firstname) + ", Grade: " + str(self.grade)
class Teacher(models.Model):

    SUBJECT =(
        ('Fine Art', 'Fine Art'),
        ('Math', 'Math'),
        ('PE/Health', 'PE/Health'),
        ('Practical Art', 'Practical Art'),
        ('English', 'English'),
        ('Social Studies', 'Social Studies'),
        ('Science', 'Science'),
    )

    firstname = models.CharField(max_length=200, null=True, verbose_name="First Name ")
    lastname = models.CharField(max_length=200, null=True, verbose_name="Last Name ")
    roomnumber = models.CharField(max_length=200, null=True, verbose_name="Room Number ")
    subject = models.CharField(max_length=200, null=True, choices=SUBJECT, verbose_name="Subject ")

    def __str__(self):
        return str(self.lastname) + ", " + str(self.firstname) + ", Subject: " + str(self.subject) + ", Room Number: " + str(self.roomnumber)