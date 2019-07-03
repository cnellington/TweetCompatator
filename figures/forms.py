from django import forms

class CompareForm(forms.Form):
	your_user = forms.CharField(label='Your Twitter username', max_length=128)
	other_user = forms.CharField(label="Your Friend's Twitter username", max_length=128)
