"""
Forms for Pinkal Rathod Personal Portfolio.
Provides a secure ModelForm for the contact page with:
- Accessible Bootstrap 5 styling
- Server-side field sanitization and validation
- Honeypot anti-spam protection
- Length and email format verification
"""

from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """
    Form for visitors to submit direct inquiries to Pinkal Rathod.
    Saves directly to ContactMessage model for administrative review.
    Includes a hidden honeypot field to automatically detect and discard bot spam.
    """
    honeypot = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'autocomplete': 'off',
            'tabindex': '-1',
            'class': 'd-none',
            'aria-hidden': 'true',
        }),
        label=''
    )

    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        labels = {
            'name': 'Full Name',
            'email': 'Email Address',
            'subject': 'Subject',
            'message': 'Your Message',
        }
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control modern-form-control',
                'placeholder': 'Enter your full name',
                'id': 'contactName',
                'required': 'required',
                'maxlength': '150',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control modern-form-control',
                'placeholder': 'Enter your email address',
                'id': 'contactEmail',
                'required': 'required',
                'maxlength': '254',
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control modern-form-control',
                'placeholder': 'Reason for contacting (e.g. Flutter Internship / Project Collaboration)',
                'id': 'contactSubject',
                'required': 'required',
                'maxlength': '200',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control modern-form-control',
                'placeholder': 'Write your message here...',
                'id': 'contactMessage',
                'rows': 5,
                'required': 'required',
                'maxlength': '5000',
            }),
        }

    def clean_name(self):
        name = self.cleaned_data.get('name', '').strip()
        if len(name) < 2:
            raise forms.ValidationError("Please provide your full name (minimum 2 characters).")
        return name

    def clean_subject(self):
        subject = self.cleaned_data.get('subject', '').strip()
        if len(subject) < 3:
            raise forms.ValidationError("Subject must be at least 3 characters long.")
        return subject

    def clean_message(self):
        message = self.cleaned_data.get('message', '').strip()
        if len(message) < 10:
            raise forms.ValidationError("Please provide a more descriptive message (at least 10 characters).")
        return message

    def clean(self):
        cleaned_data = super().clean()
        honeypot = cleaned_data.get('honeypot')
        if honeypot:
            raise forms.ValidationError("Spam submission rejected.")
        return cleaned_data
