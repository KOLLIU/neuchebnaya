from django import forms

from graf_quests.models import Character, Quest, QuestPoint


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        # fields = "__all__"
        fields = ["name", "role", "prep", "description", "stuff", "todo", "x", "y"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"}),
            "prep": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "stuff": forms.TextInput(attrs={"class": "form-control"}),
            "todo": forms.TextInput(attrs={"class": "form-control"}),
            "x": forms.TextInput(attrs={"class": "form-control"}),
            "y": forms.TextInput(attrs={"class": "form-control"}),
        }


class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ["title", "description"]
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5})
        }


class QuestPointForm(forms.ModelForm):
    class Meta:
        model = QuestPoint
        fields = ["step", "character", "description", "stuff", "todo"]
        widgets = {
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "stuff": forms.TextInput(attrs={"class": "form-control"}),
            "todo": forms.TextInput(attrs={"class": "form-control"}),
        }


class FireForm(forms.Form):
    nums = forms.IntegerField(label="Количество спрайтов")
    min_speed = forms.IntegerField(label="Минимальная скорость")
    max_speed = forms.IntegerField(label="Максимальная скорость")
    pow = forms.IntegerField(label="Степень графика")
    alt = forms.IntegerField(label="Ускорение")


class RainbowForm(forms.Form):
    speed = forms.IntegerField(label="Скорость")


class FillForm(forms.Form):
    r = forms.IntegerField(label="Красный")
    g = forms.IntegerField(label="Зелёный")
    b = forms.IntegerField(label="Синий")
