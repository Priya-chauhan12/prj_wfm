from django import forms
from FoodForAll.models import feedback

class uploadinfo(forms.ModelForm):
    class Meta:
        model = feedback
        fields = '__all__'