from django import forms


class Cipher_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

class Portal_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))

