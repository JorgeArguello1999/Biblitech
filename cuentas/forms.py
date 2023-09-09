from django.forms import ModelForm
from .models import Counts

class CountsForm(ModelForm):
    class Meta:
        model = Counts
        fields = [
            'grade', 'teacher', 'mount', 'payed', 'teacher'
        ]