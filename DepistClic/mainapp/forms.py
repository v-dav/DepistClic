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
            1,
            message='La valeur doit être supérieure à zéro')]
    )
    question_order = forms.IntegerField(widget=forms.HiddenInput())


class AnswerSex(forms.Form):
    RESPONSE_CHOICES = [
        ('Femme', 'Femme'),  # Oui est associé à Femme
        ('Homme', 'Homme'),  # Non est associé à Homme
    ]

    response = forms.ChoiceField(
        choices=RESPONSE_CHOICES,
        widget=forms.RadioSelect,
        label=''
    )

    question_order = forms.IntegerField(widget=forms.HiddenInput())
