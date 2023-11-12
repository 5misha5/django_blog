from django import forms
from .models import Post, Category


class PostForm(forms.ModelForm):
    class Meta:
        choices = Category.objects.all().values_list("name", "name")
        choice_list = [i for i in choices]

        model = Post
        fields = ["title", "author", "category", "body", "header_image"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "author": forms.TextInput(attrs={"class": "form-control", "value": "", "id": "author", "type": "hidden"}),
            # "author": forms.Select(attrs={"class": "form-control"}),
            "category": forms.Select(choices=choice_list, attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "body"]

        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }
