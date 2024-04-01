from django import forms
from . import models
class Upload(forms.ModelForm):
    class Meta:
        model=models.UploadImage
        fields=['image']
    