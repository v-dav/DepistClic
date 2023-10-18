from django import forms


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
    response = forms.IntegerField(required=True, label='')
    question_order = forms.IntegerField(widget=forms.HiddenInput())
