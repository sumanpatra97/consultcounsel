from django import forms
from .models import Forum_table,Mentor,Feedback
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UserChangeForm,PasswordChangeForm

class feedbackform(forms.ModelForm):
    class Meta:
        model=Feedback
        fields=['Name','Email','Query']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'Email':forms.TextInput(attrs={'class':'form-control'}),
                 'Query':forms.Textarea(attrs={'class':'form-control'})}


class question_form(forms.ModelForm):
    class Meta:
        model=Forum_table
        fields=['question','email']
        widgets={'question':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'}),
            'email':forms.EmailInput(attrs={'rows':3,'cols':40,'class':'form-control'})}

class answer_form(forms.ModelForm):
    class Meta:
        model=Forum_table
        fields=['answer']
        widgets={'answer':forms.Textarea(attrs={'rows':3,'cols':40,'class':'form-control'})}

class account_creation_form(UserCreationForm):
    password1=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=None
    class Meta:
        model = User
        fields =['username','email']
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'email': forms.EmailInput(attrs={'class':'form-control'})}


class login_form(AuthenticationForm):
    username=forms.CharField(label="username",widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(label="password",widget=forms.PasswordInput(attrs={'class':'form-control'}))

class name_form(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class password_form(PasswordChangeForm):
    old_password=None
    new_password1=forms.CharField(label="Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    new_password2=forms.CharField(label="Confirm Newpassword",widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User

class user_change_form(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['username','email','first_name','last_name',]
        widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
                'first_name':forms.TextInput(attrs={'class':'form-control'}),
                'last_name':forms.TextInput(attrs={'class':'form-control'}),
                'email':forms.EmailInput(attrs={'class':'form-control'}),
                }

class volunter_form(forms.ModelForm):
    class Meta:
        model=Mentor
        fields=['Name','Mobileno','Email','Profession','Mentor_Img']
        widgets={'Name':forms.TextInput(attrs={'class':'form-control'}),
                'Mobileno':forms.TextInput(attrs={'class':'form-control'}),
                'Email':forms.EmailInput(attrs={'class':'form-control'}),
                'Profession':forms.TextInput(attrs={'class':'form-control'})
                }


class digitalform(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    mobileno=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
