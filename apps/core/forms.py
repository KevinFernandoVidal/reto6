from django import forms
from .models import Categoria, Sitio

class form_sito(forms.ModelForm):
    class Meta:
        model =Sitio
        fields = '__all__'
    
class from_categoria(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = '__all__'
    
