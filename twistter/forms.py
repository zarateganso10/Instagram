from django.contrib.auth.models import User
from django import forms
from twistter.models import PostText, Profile

class UserModelForm(forms.ModelForm):
    """
    A form that creates a user, with no privileges, from the given username and
    password.
    """
    error_messages = {
        'password_mismatch': "The two password fields didn't match.",
    }
    password1 = forms.CharField(label="Password",
        widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation",
        widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification.")
    email = forms.CharField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_email(self):
         email = self.cleaned_data.get("email")
         if User.objects.filter(email=email).exists():
             raise forms.ValidationError('Ja existe um usuario com este email')
         return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()

        return user


class EditUserModelForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_email(self):
        email = self.cleaned_data.get("email")
        queryset = User.objects.filter(email=email).exclude(pk=self.instance.pk)
        if queryset.exists():
            raise forms.ValidationError('Ja existe um usuario com este email')
        return email


class TextForm(forms.ModelForm):
   class Meta:
       model = PostText
       fields = ['text']

class BiografiaForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['biografia']

class Source(forms.Form):
    user = forms.CharField(label='user', max_length=100)
