from django import forms
from .models import Inote


class CreateInoteForm(forms.ModelForm):

    class Meta:
        model = Inote
        fields = '__all__'


