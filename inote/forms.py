from django import forms
from .models import Inote


class CreateInoteForm(forms.ModelForm):

    class Meta:
        model = Inote
        fields = ('title', 'text',)  # '__all__'

