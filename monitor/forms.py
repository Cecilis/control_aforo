# -*- encoding: utf-8 -*-
from django import forms
from monitor.models import Monitor


class MonitorForm(forms.ModelForm):
    id = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    camara_serial = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)
    zona_numero = forms.CharField(widget=forms.HiddenInput, required=False, initial=0)

    class Meta:
        model = Monitor
        fields =  '__all__'

    def __init__(self, *args, **kwargs):
        super(MonitorForm, self).__init__(*args, **kwargs)
        instance = getattr(self, 'instance', None)
        if instance and instance._id:
            self.fields["id"].initial = str(instance._id)
