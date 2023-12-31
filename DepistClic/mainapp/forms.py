from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import Comment


class AnswerBinary(forms.Form):
    RESPONSE_CHOICES = [
        (True, 'Oui '),
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
            message='La valeur doit être supérieure à zéro')],
        widget=forms.NumberInput(attrs={'autofocus': True, 'class': 'rounded-lg px-4 py-3'})
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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_area']
        widgets = {
            'comment_area': forms.Textarea(
                attrs={'rows': 6, 'cols': 50, 'placeholder': 'Votre commentaire ici', 'autofocus': True}
                ),  
        }
        labels = {
            'comment_area': '',
        }

