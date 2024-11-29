from django import forms
from .models import StaffModel


class StaffModelForm(forms.ModelForm):

    class Meta:
        model = StaffModel
        # fields = []
        exclude = ['created_at', 'updated_at']