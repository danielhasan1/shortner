from django import forms
from .validators import validator_url, validate_dot_com, validaotr_http

class SubmitURLForm(forms.Form):
	url = forms.CharField(
		label='',
		validators=[validator_url,validate_dot_com, validaotr_http],
		widget = forms.TextInput(
			attrs = {"placeholder": "Paste URLs here",
					 "class":"form-control"
					 }
			)
		)

	#def clean(self):
	#	cleaned_data = super(SubmitURLForm, self).clean()
	#	url = cleaned_data['url']

	#def clean_url(self):
	#	url = self.cleaned_data['url']
	#	url_validator = URLValidator()
	#	try:
	#		url_validator(url)
	#	except:
	#		raise forms.ValidationError("Invalid URL for this Field")
	#	return url