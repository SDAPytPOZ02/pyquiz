from django import forms
from django.forms import ModelForm

from pyquiz.quiz.models import (
    Question,
    Quiz
)


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['value', 'public']


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ['name', 'public', 'description']
