from django import forms
from .models import IMAGE

class IMAGEform(forms.ModelForm):
    class Meta:
        model = IMAGE
        fields = "__all__"
        labels = {'photo':''}