from django import forms


class AnswerBinary(forms.Form):
    response = forms.BooleanField(required=True, label="Réponse oui/non")
    question_order = forms.IntegerField(widget=forms.HiddenInput())


class AnswerInteger(forms.Form):
    response = forms.IntegerField(required=True, label="Réponse nombre entier")
    question_order = forms.IntegerField(widget=forms.HiddenInput())
