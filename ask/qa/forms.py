from django import forms
from . import models


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    

    def clean(self):
        return  self.cleaned_data


    def save(self):
        question = models.Question(**self.cleaned_data)
        question.author_id = 1
        question.save()
        return question


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.CharField(widget=forms.HiddenInput(), required=False)


    def clean(self):
        return self.cleaned_data


    def save(self, id):
        answer = models.Answer(**self.cleaned_data)
        answer.author_id = 1
        answer.question_id = id
        answer.save()
        return answer