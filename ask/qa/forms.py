from django import forms
from django.contrib.auth.models import User
from . import models


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    

    def clean(self):
        return  self.cleaned_data


    def save(self):
        question = models.Question(**self.cleaned_data)
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    # question_id = forms.CharField(widget=forms.HiddenInput())
    # author = forms.CharField(widget=forms.HiddenInput())


    def clean(self):
        return self.cleaned_data


    def save(self):
        answer = models.Answer(**self.cleaned_data)
        return answer
        
        # answer.save()


class SignupForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField(widget=forms.EmailInput)


    def clean_password(self):
        pass
        #make validation here
    
    def clean_email(self):
        pass
        #make validation here

    def clean(self):
        return self.cleaned_data


    def save(self):
        data = self.cleaned_data
        return data


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput) 
    password = forms.CharField(widget=forms.PasswordInput)
    

    def clean(self):
        return self.cleaned_data
        

    def save(self):
        data = self.cleaned_data
        return data