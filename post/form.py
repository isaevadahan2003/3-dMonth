from  django import forms
from  .models import BlogPost

class BlogForm(forms.ModelForm):

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data
    class Meta:
        model = BlogPost
        fields = ('title', 'description', 'image')