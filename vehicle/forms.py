from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Car, ContactMessage, UserProfile

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    type = forms.ChoiceField(choices=[
        ['client', 'Client'],
        ['dealer', 'Dealer']
    ])

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            'type'
        )

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        UserProfile.objects.create(
            user=user,
            type=self.cleaned_data['type']
        )
        return user

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = [
            'vehicleId',
            'make',
            'shortModel',
            'longModel',
            'trim',
            'derivative',
            'yearIntroduced',
            'yearDiscontinued',
            'currentlyAvailable',
            'model_pic'
        ]

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password')
