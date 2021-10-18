from django import forms
from django.forms import fields
from post.models import Image

class NewPostForm(forms.ModelForm):
    picture = forms.ImageField(required=True)
    caption = forms.CharField(widget=forms.Textarea(attrs={'class': 'input is-medium'}), required=True)
    tags = forms.CharField(widget=forms.TextInput(attrs={'class': 'input is-medium'}), required=True)

    class Meta:
        model = Image
        fields = ('picture', 'caption', 'tags' )