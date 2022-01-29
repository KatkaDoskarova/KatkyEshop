from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    city = forms.CharField()
    street = forms.CharField()
    zipcode = forms.CharField()


    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2',
            'email',
            'city',
            'street',
            'zipcode',
        ]
        help_texts = {"username": "Jmeno", "first_name": "Krestni jmeno"}

    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.city = self.cleaned_data['city']
        user.street = self.cleaned_data['street']
        user.zipcode = self.cleaned_data['zipcode']

        if commit:
            user.save()

        return user
