from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User


class Creation_user(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']



class Update_user(UserChangeForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']