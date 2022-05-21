from django import forms
from .models import BookATable, ContactUs


class BookATableForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                                'type': "text",
                                'name': "name",
                                'class': "form-control",
                                'id': "name",
                                'placeholder': "Your Name",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                           }))
    phone = forms.CharField(max_length=15,
                            widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'name': "phone",
                                'id': "phone",
                                'placeholder': "Your Phone",
                                'data-rule': "minlen:4",
                                'data-msg': "Please enter at least 4 chars"
                            }))
    persons = forms.IntegerField(widget=forms.NumberInput(attrs={
                                'type': "number",
                                'class': "form-control",
                                'name': "people",
                                'id': "people",
                                'placeholder': "# of people",
                                'data-rule': "minlen:1",
                                'data-msg': "Please enter at least 1 chars"
                            }))
    email = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={
                                'type': "email",
                                'class': "form-control",
                                'name': "email",
                                'id': "email",
                                'placeholder': "Your Email",
                                'data-rule': "email",
                                'data-msg': "Please enter a valid email"
                            }))
    date = forms.CharField(widget=forms.TextInput(attrs={
                               'type': "text",
                               'name': "date",
                               'class': "form-control",
                               'id': "date",
                               'placeholder': "Date",
                               'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars"
                           }))
    time = forms.CharField(widget=forms.TextInput(attrs={
                               'type': "text",
                               'class': "form-control",
                               'name': "time",
                               'id': "time",
                               'placeholder': "Time",
                               'data-rule': "minlen:4",
                               'data-msg': "Please enter at least 4 chars"
                           }))
    message = forms.CharField(max_length=500,
                              widget=forms.Textarea(attrs={
                                'type': "message",
                                'class': "form-control",
                                'name': "message",
                                'rows': "5",
                                'placeholder': "Message",
                                'required': "required"
                              }))

    class Meta:
        model = BookATable
        fields = ('name', 'phone', 'persons', 'email', 'date', 'time', 'message')


class ContactUsForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
                           widget=forms.TextInput(attrs={
                            'type': "text",
                            'name': "name",
                            'class': "form-control",
                            'id': "name",
                            'placeholder': "Your Name",
                            'required': "required"
                           }))
    email = forms.CharField(max_length=50,
                            widget=forms.TextInput(attrs={
                                'type': "email",
                                'class': "form-control",
                                'name': "email",
                                'id': "email",
                                'placeholder': "Your Email",
                                'required': "required"
                            }))
    subject = forms.CharField(max_length=60,
                              widget=forms.TextInput(attrs={
                                'type': "text",
                                'class': "form-control",
                                'name': "subject",
                                'id': "subject",
                                'placeholder': "Subject",
                                'required': "required"
                              }))
    message = forms.CharField(max_length=500,
                              widget=forms.Textarea(attrs={
                                    'type': "message",
                                    'class': "form-control",
                                    'name': "message",
                                    'rows': "5",
                                    'placeholder': "Message",
                                    'required': "required"
                              }))

    class Meta:
        model = ContactUs
        fields = ('name', 'email', 'subject', 'message')
