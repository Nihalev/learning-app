from django import forms
from myapp.models import Textbooks



class TextbookForm(forms.ModelForm):
    
    class Meta:
        model = Textbooks
        fields = '__all__'

        