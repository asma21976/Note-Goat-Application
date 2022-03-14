from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name',)
        '''
        Temporarily got rid of phone number until I can figure out how to get rid of the +1
        '''

