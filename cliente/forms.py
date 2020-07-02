# -*- encoding: utf-8 -*-
from django import forms
from cliente.models import Cliente



class ClienteForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Cliente
        fields =  '__all__'
        #exclude = ('id_cliente',)

    def __init__(self, *args, **kwargs):
        super(ClienteForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)


class ClienteTodosForm(forms.ModelForm):
    clientes = forms.ChoiceField(widget=forms.Select, choices=Cliente.objects.all(), required=False, help_text="clientes")

    class Meta:
        model = Cliente
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        print('oooo')