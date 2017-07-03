from django import forms
from urly.models import ShortUrl


class URLyForm(forms.ModelForm):

    class Meta:
        model = ShortUrl
        fields = ['target']

    # Target can be empty in model but not in form
    def clean_target(self):
        if len(str(self.cleaned_data['target']).strip()) == 0:
            raise forms.ValidationError("URL can not be empty!")
        return self.cleaned_data['target']
