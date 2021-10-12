from django import forms
from django.forms import fields
from visitantes.models import Visitante

class VisitanteForm(forms.ModelForm):
    class Meta:
        model = Visitante
        fields = [
            "nome_completo", "cpf", "data_nascimento", 
            "numero_casa", "placa_veiculo"
        ]

