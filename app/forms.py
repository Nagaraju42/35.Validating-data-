from django import forms


def check_for_n(value):
    if value[0].lower()=='n':
       raise forms.ValidationError('name start with n')
 

class StudentForm(forms.Form):
    name=forms.CharField(max_length=100,validators=[check_for_n])
    age=forms.IntegerField()
    email=forms.EmailField()
