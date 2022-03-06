from django.forms import ModelForm
from .models import classData

class classForm(ModelForm):
    class Meta:
        model = classData
        fields = '__all__' 