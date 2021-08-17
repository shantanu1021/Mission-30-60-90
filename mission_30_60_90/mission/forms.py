from django import forms
from django.contrib.auth.models import User
from .models import Missions,Status

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['is_done','remarks']