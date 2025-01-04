from django import forms
from testing.models import Contact, Newsletter

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
    

class TestForm(forms.ModelForm):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    subject = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)
    
    
class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'