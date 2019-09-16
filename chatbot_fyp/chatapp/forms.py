from django import forms
from chatapp.models import Contact

class ContactForm(forms.ModelForm):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder": "Sushil Shrestha"}))
	email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder": "abc@gmail.com"}))
	subject = forms.CharField(max_length=50, widget=forms.TextInput(attrs={"placeholder": "Subject"}))
	message = forms.CharField(
			required = True,
			widget=forms.Textarea(
				attrs= {
					"placeholder": "You can enter your message"
				})
		)

	class Meta:
		model = Contact
		fields = ['name', 'email', 'subject', 'message']