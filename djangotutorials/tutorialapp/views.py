from django.shortcuts import render

# Create your views here.

def base(request):
    context={

    }

    return render(request, 'base.html', context)
def home(request):
    context={

    }

    return render(request, 'home.html', context)