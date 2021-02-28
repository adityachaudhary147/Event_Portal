
from django import forms
from .models import Model_Event


class Model_Event_Form(forms.ModelForm):
    class Meta:
        model = Model_Event
        fields = ['event_name','data','time','location','image']
