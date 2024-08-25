# main/forms.py

from . import models
from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = models.CustomUser
		fields = ('email', 'password1', 'password2')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['email'].widget.attrs.update({'class': 'form-control'})
