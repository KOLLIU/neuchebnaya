from django import forms

from graf_quests.models import Character, Quest, QuestPoint


class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        # fields = "__all__"
        fields = ["name", "role", "description", "stuff", "todo"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "role": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 5}),
            "stuff": forms.TextInput(attrs={"class": "form-control"}),
            "todo": forms.TextInput(attrs={"class": "form-control"}),
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
    #
    # def __init__(self, *args, **kwargs):
    #     super(QuestPointForm, self).__init__(*args, **kwargs)
    #     if self.quest:
    #         self.fields["character"].queryset = Character.objects.filter(game=self.quest.game)

# class CharacterFormOLD(forms.Form):
#     game = forms.ModelChoiceField(queryset=Game.objects.all(), empty_label="Игра", label="Игра",
#                                   widget=forms.Select(attrs={"class": "form-control"}))
#
#     name = forms.CharField(max_length=64, label="Имя", required=False,
#                            widget=forms.TextInput(attrs={"class": "form-control"}))
#
#     role = forms.CharField(max_length=256, label="Роль", required=False,
#                            widget=forms.TextInput(attrs={"class": "form-control"}))
#
#     description = forms.CharField(label="Описание", required=False,
#                                   widget=forms.Textarea(attrs={"class": "form-control"}))
#
#     x = forms.IntegerField(initial=500)
#     y = forms.IntegerField(initial=500)
