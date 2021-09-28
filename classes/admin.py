from django.contrib import admin
from .models import GymClass, Category, Trainer, Timetable

admin.site.register(GymClass)
admin.site.register(Category)
admin.site.register(Trainer)
admin.site.register(Timetable)

