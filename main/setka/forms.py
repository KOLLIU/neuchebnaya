from django import forms

from setka.models import File


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        # fields = "__all__"
        fields = ["file", "title"]
        widgets = {"title": forms.TextInput(attrs={"class": "form-control"}),
                   "file": forms.FileInput(attrs={"class": "form-control"})}
