# Note-Goat-Application
Group project for SENG 401 - Software Architecture

## Description

This Django project includes the backend, frontend, and tests 
for a note taking web application. The application is for 
registered users to write notes, organize them in folders, and 
share the notes. Users can also view or edit other user’s notes 
if they are shared with them. This is all done through the usage 
of accounts. Users may create their own account through the sign
up page.

## Usage

The site has been deployed on https://note-goat-site.herokuapp.com/
where the full website can be accessed. However, if you would like
to run the site locally, simply follow the following instructions:

We assume that you have Python 3 installed on your machine.

To run this program, start by setting up a python virtual 
environment in the folder where Note-Goat-Application-Frontend-
resides. This can be done by running 
```
python3 -m venv CPSC471Project
source CPSC471Project/bin/activate
```
on Mac/Linux or 
```
pip install virtualenv
python -m virtualenv . 
.\scripts\activate
```
on Windows. You may need to run `.\scripts\activate` twice;
you will know it worked when your command prompt starts with
parentheses, like this:
```
(Note-Goat-Application-Frontend-) username@computer seng401 %
```

Next, we have to install Django, using 
```
python -m pip install Django
```
on Mac/Linux or
```
py -m pip install Django
```
on Windows. If you have run into any issues so far, consult
https://docs.djangoproject.com/en/3.2/intro/install/ or
https://docs.djangoproject.com/en/3.2/topics/install/#installing-official-release

Finally, you must install some of the extensions we use in this project:
```
pip install django-crispy-forms
pip install whitenoise
pip install django-tinymce
```

Now it is time to set up the server. Navigate to the inner
folder containing `manage.py`. Then run
```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
and in the browser of your choice, go to
http://127.0.0.1:8000/
where you should see a welcome page. 

From here, you can navigate to the webpages of our Note Goat site.
