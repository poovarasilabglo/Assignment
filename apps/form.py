from django import forms
from .models import student
from .models import mark


class studentform(forms.ModelForm):
    class Meta:
        model = student
        fields = "__all__"
        
        
class markform(forms.ModelForm):
    class Meta:
        model = mark
        fields = "__all__"
