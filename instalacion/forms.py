from django import forms
from instalacion.models import Instalacion


class InstalacionAddForm(forms.ModelForm):
    class Meta:
        model = Instalacion
        fields = "__all__"
        exclude = ('monitores','camara_zonas',)


class InstalacionForm(forms.ModelForm):
    id_registro = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Instalacion
        fields = "__all__"
        #exclude = ('camara_zonas',)

    def __init__(self, *args, **kwargs):
        super(InstalacionForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields["id_registro"].initial = instance.id

