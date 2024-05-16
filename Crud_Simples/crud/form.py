from django import forms
from .models import Calcado

class FormCadProduto(forms.ModelForm):
    #Choices
    marcas_choices = [
    ('Nike', 'Nike'),
    ('Adidas', 'Adidas'),
    ('Penalti', 'Penalti'),
    ('Vans', 'Vans'),
    ('Mizuno', 'Mizuno'),
    ('Olimpicus', 'Olimpicus'),
]
    class Meta:
        model = Calcado
        fields = ['nome', 'preco', 'estoque', 'tamanho', 'descricao','marca']
    nome = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Digite um Nome', 'id':'IdNameInput'}))
    preco = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Preço'}))
    estoque = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Estoque Disponível'}))
    tamanho = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Tamanho Disponível'}))
    descricao = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Descrição do calçado'}), max_length=100)
    marca = forms.ChoiceField(choices=marcas_choices, widget=forms.Select(attrs={'class':'form-control', 'placeholder':'Marca'}))


