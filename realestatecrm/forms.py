from django import forms

from realestatecrm.models import Realestate

class RealestateForm(forms.ModelForm):

    class Meta:

        model=Realestate

        fields="__all__"