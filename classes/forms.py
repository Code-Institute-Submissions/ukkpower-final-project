from django import forms
from .models import GymClass, Category

class ClassForm(forms.ModelForm):

    class Meta:
        model = GymClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]