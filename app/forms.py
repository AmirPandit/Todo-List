from django import forms
from .models import formdataset, Login

class FormList(forms.ModelForm):
    class Meta:
        model = formdataset
        fields = ['Title', 'Description', 'Date']

        widgets = {
            'Title': forms.TextInput(attrs={
                'placeholder': 'Title',
            }),
            'Description' : forms.Textarea(attrs={
                'placeholder': 'Things to note..',
                'rows': 3
            }),
            'Date': forms.DateInput(attrs={
                'type': 'date',
            })
        }
class LoginList(forms.ModelForm):
    class Meta:
        model = Login
        fields = ['username', 'password']