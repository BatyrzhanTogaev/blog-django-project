from django import forms
from .models import Post, Category


class PostForms(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'category']


class PostFillerForms(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        required=False,
        empty_label='Все категории'
    )

    class Meta:
        model = Post
        fields = ['category']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.all() 
