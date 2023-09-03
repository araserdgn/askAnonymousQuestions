
from django.forms import ModelForm, TextInput, Textarea
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['nickname','isim','resim','email']
    
        labels = {
        'nickname': 'Nickname Etiketi',
        'isim': 'İsim Etiketi',
        'resim': 'Resim Etiketi',
        'email': 'Email Etiketi',
    }

    def __init__(self,*args,**kwargs):
        super(ProfileForm,self).__init__(*args,**kwargs)
        for name, field in self.fields.items():
            field.widget.attrs.update({'class':'form-control'})