from django import forms
# from .models import Optimiseruser

class Qviz_it_iitb_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # member2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)

class Qviz_it_non_iitb_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    # member2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)