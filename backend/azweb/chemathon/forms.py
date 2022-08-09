from django import forms
from . import models


class QuestionForm(forms.ModelForm):

    #this will show dropdown __str__ method course model is shown on html so override it
    #to_field_name this will fetch corresponding value  user_id present in course model and return it
    # courseID=forms.ModelChoiceField(queryset=models.Course.objects.all(),empty_label="Course Name", to_field_name="id")
    class Meta:
        model=models.Chemathon_questions_admin
        fields=['q1','q2','q3','q4','q5','q6','q7']
        widgets = {
            'q1': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q2': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q3': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q4': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q5': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q6': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
            'q7': forms.Textarea(attrs={'rows': 3, 'cols': 50}),
        }


class Chemathon_questions_admin_Form(forms.Form):
     q1 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q2 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q3 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q4 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q5 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q6 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
     q7 = forms.Textarea(attrs={'rows': 3, 'cols': 50})
class Chemathon_questions_Form(forms.Form):
    team_id = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}),required=True)
    question1 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question2 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question3 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question4 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question5 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question6 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)
    question7 =  forms.FloatField(widget=forms.TextInput(attrs={'class':'form-control'}),required=False)


class Chemathon_Form(forms.Form):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member1 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    member2 = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
