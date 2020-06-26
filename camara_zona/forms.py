from django import forms
from camara_zona.models import CamaraZona


class CamaraZonaForm(forms.ModelForm):
    class Meta:
        model = CamaraZona
        fields = "__all__"
