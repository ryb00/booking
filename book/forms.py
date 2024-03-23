from .models import Schedule
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['date_of_visit', 'time_of_visit', 'number_of_visitors', 'number_of_hours']
        widgets = {
            'date_of_visit': forms.DateInput(attrs={'type': 'date'}),
        }
        
