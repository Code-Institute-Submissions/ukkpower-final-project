from django import forms
from .models import GymClass, Category, Trainer, Timetable


class ClassForm(forms.ModelForm):

    class Meta:
        model = GymClass
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]


class TrainerForm(forms.ModelForm):

    class Meta:
        model = Trainer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class TimetableForm(forms.ModelForm):

    class Meta:
        model = Timetable
        fields = '__all__'
        widgets = {
            'day': forms.Select(
                choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'),
                         ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'),
                         ('Friday', 'Friday'), ('Saturday', 'Saturday'),
                         ('Sunday', 'Sunday')]),
            'time_slot': forms.Select(
                choices=[('9:00 am', '9:00 am'), ('10:00 am', '10:00 am'),
                         ('11:00 am', '11:00 am'), ('12:00 pm', '12:00 pm'),
                         ('1:00 pm', '1:00 pm'), ('2:00 pm', '2:00 pm'),
                         ('3:00 pm', '3:00 pm'), ('4:00 pm', '4:00 pm'),
                         ('5:00 pm', '5:00 pm'), ('6:00 pm', '6:00 pm'),
                         ('7:00 pm', '7:00 pm')]),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
