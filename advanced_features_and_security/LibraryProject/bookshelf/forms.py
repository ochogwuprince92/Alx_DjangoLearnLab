from django import forms
from .models import Book  # Adjust this based on your model

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Book  # Adjust this to the model you're using
        fields = ['title', 'author', 'published_date']  # Adjust this to the fields you want to include
class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
