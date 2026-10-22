"""
Forms for Pinkal Rathod Personal Portfolio.
Provides a secure Form for the contact page with:
- Accessible Bootstrap 5 styling
- Server-side field sanitization and validation
- Honeypot anti-spam protection
- Length and email format verification
- Zero database dependency
"""

from django import forms


class ContactMessageData:
    """Lightweight data object representing a validated contact message."""
    def __init__(self, name, email, subject, message):
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message


class ContactForm(forms.Form):
    """
    Form for visitors to submit direct inquiries to Pinkal Rathod.
    Includes a hidden honeypot field to automatically detect and discard bot spam.
    Operates without database writes for serverless/read-only deployment.
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
    name = forms.CharField(
        max_length=150,
        required=True,
        label='Full Name',
        widget=forms.TextInput(attrs={
            'class': 'form-control modern-form-control',
            'placeholder': 'Enter your full name',
            'id': 'contactName',
            'required': 'required',
            'maxlength': '150',
        }),
    )
    email = forms.EmailField(
        max_length=254,
        required=True,
        label='Email Address',
        widget=forms.EmailInput(attrs={
            'class': 'form-control modern-form-control',
            'placeholder': 'Enter your email address',
            'id': 'contactEmail',
            'required': 'required',
            'maxlength': '254',
        }),
    )
    subject = forms.CharField(
        max_length=200,
        required=True,
        label='Subject',
        widget=forms.TextInput(attrs={
            'class': 'form-control modern-form-control',
            'placeholder': 'Reason for contacting (e.g. Flutter Internship / Project Collaboration)',
            'id': 'contactSubject',
            'required': 'required',
            'maxlength': '200',
        }),
    )
    message = forms.CharField(
        max_length=5000,
        required=True,
        label='Your Message',
        widget=forms.Textarea(attrs={
            'class': 'form-control modern-form-control',
            'placeholder': 'Write your message here...',
            'id': 'contactMessage',
            'rows': 5,
            'required': 'required',
            'maxlength': '5000',
        }),
    )

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

    def save(self, commit=True):
        """Returns message data object without hitting the database."""
        return ContactMessageData(
            name=self.cleaned_data.get('name', ''),
            email=self.cleaned_data.get('email', ''),
            subject=self.cleaned_data.get('subject', ''),
            message=self.cleaned_data.get('message', ''),
        )
