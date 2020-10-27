from django import forms
from .models import ImageUpload

class ImageForm(forms.ModelForm):
    """ Form for the image model """
    class Meta:
        model = ImageUpload
        fields = ('title','image')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Entrer le nom du client'})
        }