from django import forms
from . import  models
from django.forms.widgets import Textarea

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['doc_type','doc_num','email',
                'first_name','last_name']

class ClaimForm(forms.ModelForm):
    class Meta:
        model= models.Claim
        fields=('reception_mean','type','cause',
                'description','inmediate_solution')
        widgets={
            'description': Textarea(attrs={'cols':80,'rows':20})
        }

class TypeClaimForm(forms.ModelForm):
    type=forms.CharField(required=True)
    class Meta:
        model = models.Claim
        fields=['type']

    def save(self, commit=True):
        instance= super(TypeClaimForm,self).save(commit=False)
        instance.claim.type=self.cleaned_data['type']
        if  commit:
            instance.claim.save()
        return instance