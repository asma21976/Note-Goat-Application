from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

'''
The sign up page should ask for the fields: email, username, first_name, and last_name
to create a new user and sign up for the website
'''
class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name',)

