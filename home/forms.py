from django import forms
from django.utils.translation import gettext_lazy as _


class PostSearchForm(forms.Form):
    search = forms.CharField(
        widget=forms.TextInput(
            attrs=({'class': "form-control mt-3", 'type': "search", 'placeholder': _('به دنبال چه می‌گردید؟'), 'aria-label': "Search",
                    'style': "height: 38px;margin-top: 15px;margin-right: 5px"})), label='')
