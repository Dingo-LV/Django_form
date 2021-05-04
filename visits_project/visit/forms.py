from django import forms
from visit.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            # 'firstname',
            # 'lastname',
            'username',
            'email',
        ]