from django import forms
from .models import *

class SwitchForm(forms.ModelForm):
    class Meta:
        model = Switch
        fields = ('type', 'model', 'status', 'issues')



class ApForm(forms.ModelForm):
    class Meta:
        model = Ap
        fields = ('type', 'model', 'status', 'issues')


class PowerSupplyForm(forms.ModelForm):
    class Meta:
        model = PowerSupply
        fields = ('type', 'model', 'status', 'issues')