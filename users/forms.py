from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import User

class SignupForm(forms.Form):
	username=forms.CharField(min_length=4,max_length=50)
	password=forms.CharField(max_length=70, widget=forms.PasswordInput())
	password_confirmation=forms.CharField(max_length=70, widget=forms.PasswordInput())

	first_name=forms.CharField(min_length=2, max_length=50)
	last_name=forms.CharField(min_length=2, max_length=50)

	email=forms.CharField(min_length=6, max_length=20)
	widget=forms.EmailInput()


	def clean_username(self):
		username = self.clean_data["username"]
		username_taken=User.object.filter(username=username).exists()
		if username_taken:
			raise forms.ValidationError("Sorry, this Username is in use")
		return username

	def clean(self): #password validation
		data= super().clean()
		password = data["password"]
		password_confirmation = data["password_confirmation"]

		if password != password_confirmation:
			raise forms.ValidationError("Password do not match")

class ProfileForm(forms.Form):
    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
