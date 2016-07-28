from django import forms
#from django_countries.fields import CountryField
from django_countries import countries

class JoinForm(forms.Form):

	# choice_options = (
	# 		(1, "I want to create a young coders' club"),
	# 		(2, "I want to volunteer"),
	# 	)

	first_name = forms.CharField(required=True, max_length=100)
	last_name = forms.CharField(required=True, max_length=100)
	email = forms.EmailField(required=True)
	country = forms.ChoiceField(choices=list(countries))
	state = forms.CharField(required=True, max_length=100)
	# address = forms.CharField(required=True, max_length=100)
	phonenumber = forms.CharField(required=True)
	#join_option = forms.CharField(choices=choice_options,default="Pick an option")
	
	def __init__(self, *args, **kwargs):
	  super(JoinForm, self).__init__(*args, **kwargs)   
	  self.base_fields['country'].initial = "Select a country"