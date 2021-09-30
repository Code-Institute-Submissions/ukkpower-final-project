from django.contrib import admin
from .models import GymClass, Category, Trainer, Timetable
from django import forms


class TimetableForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Timetable
        widgets = {
            'day': forms.Select(choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')]),
            'time_slot': forms.Select(choices=[('9:00 am', '9:00 am'), ('10:00 am', '10:00 am'), ('11:00 am', '11:00 am'), ('12:00 pm', '12:00 pm'), ('1:00 pm', '1:00 pm'), ('2:00 pm', '2:00 pm'), ('3:00 pm', '3:00 pm'), ('4:00 pm', '4:00 pm'), ('5:00 pm', '5:00 pm'), ('6:00 pm', '6:00 pm'), ('7:00 pm', '7:00 pm')]),
        }


class TimetableAdmin(admin.ModelAdmin):
    form = TimetableForm


admin.site.register(GymClass)
admin.site.register(Category)
admin.site.register(Trainer)
admin.site.register(Timetable, TimetableAdmin)
