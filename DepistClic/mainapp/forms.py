from django import forms
from .models import Answer


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = [
            'answer_text',
            'question',
        ]
        widgets = {
            'question': forms.HiddenInput()
        }
