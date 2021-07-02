from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import UserProfile


class UserProfileCreationForm(UserCreationForm):

    class Meta:
        model = UserProfile
        fields = ('email','full_name','mob_number','profile_photo')

class UserProfileChangeForm(UserChangeForm):

    class Meta:
        model = UserProfile
        fields = ('email',)
