from django import forms

from faunatrack.models import Observation

class ObservationForm(forms.ModelForm):
    class Meta:
        model = Observation
        fields = "__all__"