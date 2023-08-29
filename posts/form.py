from django import forms
from .models import Comment
from django.utils.translation import gettext_lazy as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body',)
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control validate-review textarea',
                    'placeholder': _('نظر خود را بنویسید'),
                    "rows": 3,
                    "cols": 40,
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control validate-name textinput textInput',
                    "placeholder": _('مثال : مهران میرزائي'),
                    "style": "padding:5px 16px;border-radius:9px"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control validate-name textinput textInput',
                       "placeholder": _('مثال : mehranmirzaeiv@gmail.com'),
                       "style": "padding:5px 16px;border-radius:9px"}),

        }


class ReplyCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body', 'parent')
        widgets = {
            'body': forms.Textarea(
                attrs={
                    'class': 'form-control validate-review textarea',
                    'placeholder': _('نظر خود را بنویسید'),
                    "rows": 3,
                    "cols": 40,
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-control validate-name textinput textInput',
                    "placeholder": _('مثال : مهران میرزائي'),
                    "style": "padding:5px 16px;border-radius:9px"}),
            'email': forms.EmailInput(
                attrs={'class': 'form-control validate-name textinput textInput',
                       "placeholder": _('مثال : mehranmirzaeiv@gmail.com'),
                       "style": "padding:5px 16px;border-radius:9px"}),
            'parent': forms.HiddenInput()
        }
