from django.forms import ModelForm
from django import forms
from .models import Job,Company

JOB_TYPE = (("1", "Full time"), ("2", "Part time"), ("3", "Internship"))

class DateInput(forms.DateInput):
    input_type = "date"


class JobCreateForm(ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Job title'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Delhi, India'}))
    type = forms.ChoiceField(choices=JOB_TYPE,initial='1')
    link = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'www.microsoft.com/career/ka?=22 '}))
    salary = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12.5 lacs'}))
    # tags
    class Meta:
        model = Job
        exclude = ["created","host"]
        widgets = {"last_date": DateInput()}

class CompanyCreateForm(ModelForm):
    class Meta:
        model = Company
        exclude = ["created"]