# django-tutorial

## Step 1: Create a project
-> python -m django startproject djangotutorials
## Step 2: create an app
- django-admin startapp djangotutorials
- python manage.py startapp djangotutorials
## step 3: Run Web Server
- cd into the project folder where manage.py is located
- run `python manage.py runserver`
## Step 4: build database
- cd into folder with manage.py
- `python manage.py migrate`
## Step 5: create superuser
- cd into manage.py folder
- python manage.py createsuperuser
##step 6: add app to settings installed apps dictionary
- 'installed _apps = [
- ' ...
- app_name',
## step 7: add templates folder
- 'DIRS': [BASE_DIR / 'templates'],'
## view function
```python
def base(request):
    context={

    }

    return render(request, 'base.html', context)
```
step 8: add apps urls.py to project urls.py
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tutorialapp.urls')),
]
```
## step 9: add app's urls.py to app's folder
```python
from django.urls import path, include
from .  import views

urlpatterns = [
    path('base/', views.base, name='base'),
]
```
## Inheriting code from a template
```
{% extends 'base.html' %}

{% block content%}

<br><br><br>

<h1> This is the homepage! </h1>
{% endblock %}
```
## Making changes to the database
### saving changes
```
python manage.py makemigrations
```
## step 2: build changes into the database
```
python manage.py migrate
```
