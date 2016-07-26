from django import forms

class ContactForm(forms.Form):
	first_name = forms.CharField(required=True, max_length=100)
	second_name = forms.CharField(required=True, max_length=100)
	message = forms.CharField(
		required = True,
		widget=forms.Textarea)
	sender = forms.EmailField(required=True)
	

class JoinusForm():
	country  = forms.ChoiceField(required = False)
	