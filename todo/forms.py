from django import forms
from django.forms import SelectDateWidget

from todo.models import Tag, Task


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    deadline = forms.DateField(
        widget=SelectDateWidget(empty_label="Nothing")
    )

    class Meta:
        model = Task
        fields = "__all__"
