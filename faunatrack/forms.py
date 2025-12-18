from django import forms

from faunatrack.models import Observation

class FaunatrackForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super(FaunatrackForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'border rounded-lg focus:ring-blue-500 focus:border-blue-500 w-full p-2.5'
    

class ObservationForm(FaunatrackForm):
    class Meta:
        model = Observation
        fields = "__all__"
        widgets = {
            "date_observation": forms.widgets.DateInput(
                attrs={
                    "type": "date"
                }
            )
        }