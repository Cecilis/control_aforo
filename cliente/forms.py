from django import forms
from cliente.models import Cliente


class ClienteForm(forms.ModelForm):
    id_registro = forms.IntegerField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = Cliente
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance.id:
            self.fields["id_registro"].initial = instance.id