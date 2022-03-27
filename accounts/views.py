from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

'''
When signing up, the form, CustomUserCreationForm should be used
After successfully signing in, it should take the user to the login page so they can log in
The html file for the sign up page is in templates/registration/signup.html
'''
class SignupPageView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
