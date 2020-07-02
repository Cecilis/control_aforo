# -*- encoding: utf-8 -*-
from django import forms
from camara_zona.models import CamaraZona


class CamaraZonaForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = CamaraZona
        fields = '__all__'
        exclude = ('id_camara_zona',)

    def __init__(self, *args, **kwargs):
        super(CamaraZonaForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            #self.fields["id_camara_zona"].initial = " _0"

class CamaraZonaEditarForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial='')
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = CamaraZona
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CamaraZonaEditarForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
            arr_camara_zona = instance.id_camara_zona.split('_')
            if len(arr_camara_zona)>1:
                self.fields["camara_serial"].initial = str(arr_camara_zona[0]).upper()
                self.fields["zona_numero"].initial = arr_camara_zona[1]