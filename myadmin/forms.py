from django import forms
from .models import myLoginDetials,myUserDetials,myscreenshot


#inbuilt form for adding app detials
class LoginDetials(forms.ModelForm):
    app_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'App Name'}))
    app_link=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Link Name'}))
    points_amount=forms.DecimalField(widget=forms.NumberInput(attrs={'placeholder': 'Add Points'}))
    class Meta:
        model=myLoginDetials
        fields=['image','app_name','app_link','app_category','sub_category','points_amount']
        labels = {'image':'Add Icon','app_name':'Enter Name','app_link':'App Link','app_category':'Select categories','sub_category':'Select Sub_Category','points_amount':'Add Points'}
        widget={
        'app_name':forms.TextInput(attrs={'class':'form-control'}),
        'app_link':forms.TextInput(attrs={'class':'form-control'}),
        'app_category':forms.Select(attrs={'class':'form-select'}),
        'sub_category':forms.Select(attrs={'class':'form-select'}),
        'points_amount':forms.NumberInput(attrs={'class':'form-control'}),
        }

#inbuilt form for adding user credentials
class userLoginDetials(forms.ModelForm):
    
    class Meta:
        model=myUserDetials
        fields=['username','password']


#form for screenshot 
class userscreenshot(forms.ModelForm):
    class Meta:
        model=myscreenshot
        fields='__all__'  
        