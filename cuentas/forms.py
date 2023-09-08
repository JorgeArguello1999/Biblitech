from django.forms import ModelForm
from .models import Counts

class CountsForm(ModelForm):
    model = Counts
    fields = [
        'grade', 'teacher', 'mount', 'payed', 'teacher'
    ]