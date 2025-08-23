
from django import forms
from .models import registrations

class registration_forms(forms.ModelForm):

    Pass= forms.CharField(min_length=6)
    Repass=forms.CharField(min_length=6)
    
    class Meta:
        model = registrations
        fields = ['Name', 'Email', 'Pass', 'Repass']



class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = registrations
        fields = ['Name', 'Email', 'profile_pic']    



 

    def clean(self):
     cleaned_data = super().clean()
     Pass_match = cleaned_data.get('Pass')
     Repass_match = cleaned_data.get('Repass')
     if Pass_match and Repass_match:
        if Pass_match != Repass_match: 
            raise forms.ValidationError("Enter your correct pass")
     return cleaned_data
             
          
    def clean_pass(self):
        pass_validation = self.cleaned_data['Pass']
        if len(pass_validation)<4:
         raise forms.ValidationError('Enter your correct pass')
        return pass_validation  
           

      







        




    
        
   