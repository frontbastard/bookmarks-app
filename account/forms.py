from django import forms
from django.contrib.auth import get_user_model


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput
    )

    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "email"]

    def clean_password2(self):
        cd = self.cleaned_data

        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]

    def clean_email(self):
        cd = self.cleaned_data
        email_exists = get_user_model().objects.filter(email=cd["email"]).exists()

        if email_exists:
            raise forms.ValidationError("User with this email already exists.")
        return cd["email"]
