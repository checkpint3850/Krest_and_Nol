from django import forms
from django.core.exceptions import ValidationError
from .models import Post


class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'heading',
            'text',
            'author',
            'category',
        ]

    def clean_name(self):
        heading = self.cleaned_data["heading"]
        if heading[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )
        return heading
