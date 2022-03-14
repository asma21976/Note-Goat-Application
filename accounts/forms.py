from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'first_name', 'last_name',
                  'address_line_1', 'address_line_2', 'city', 'province_state',
                  'postal_code', 'country')
        '''
        Temporarily got rid of phone number until I can figure out how to get rid of the +1
        '''

