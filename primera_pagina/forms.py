from django import forms
from .models import Autor, Libro, Editorial

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = '__all__'


class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__'


class EditorialForm(forms.ModelForm):
    class Meta:
        model = Editorial
        fields = '__all__'

class BuscarForm(forms.Form):
    query = forms.CharField(label='Buscar', max_length=150)