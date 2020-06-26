from django import forms
from monitor.models import Monitor


class MonitorForm(forms.ModelForm):
    class Meta:
        model = Monitor
        fields = "__all__"
