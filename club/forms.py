from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=120,
        label='Your name',
        widget=forms.TextInput(attrs={
            'placeholder': 'Name',
            'class': 'input-field',
        }),
    )
    message = forms.CharField(
        label='Message',
        widget=forms.Textarea(attrs={
            'placeholder': 'Type your message here...',
            'class': 'input-field',
            'rows': 6,
        }),
    )
