import datetime

from django import forms

from base.models import Players
from base.models import StatPlayerRegistration



class MailFormFilter(forms.Form):
    email = forms.EmailField(max_length=Players._meta.get_field('email').max_length)

class ExpFormChange(forms.Form):
    xp = forms.IntegerField(required=True)

class DateForm(forms.Form):
    fromdate = forms.DateField(required=False, input_formats=['%Y-%m-%d','%m/%d/%Y','%m/%d/%y','%d-%m-%Y'],
                               widget = forms.TextInput(attrs={'placeholder': '01-01-2015'}))
    todate = forms.DateField(required=False, input_formats=['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%d-%m-%Y'],
                               widget=forms.TextInput(attrs={'placeholder': '01-01-2017'}))



