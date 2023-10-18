from django import forms
from django.core.validators import MinValueValidator


class AnswerBinary(forms.Form):
    RESPONSE_CHOICES = [
        (True, 'Oui'),
        (False, 'Non'),
    ]

    response = forms.ChoiceField(
        choices=RESPONSE_CHOICES,
        widget=forms.RadioSelect,
        label=''
    )

    question_order = forms.IntegerField(widget=forms.HiddenInput())


class AnswerInteger(forms.Form):
    response = forms.IntegerField(
        required=True,
        label='',
        validators=[MinValueValidator(
            0,
            message='La valeur doit être supérieure ou égale à zéro')]
    )
    question_order = forms.IntegerField(widget=forms.HiddenInput())
