from django.urls import path
from . import views

urlpatterns = [
    path('gym_classes', views.gym_classes, name='gym_classes'),
    path('gym_class/<int:class_id>/', views.gym_class, name='gym_class'),
    path('timetable', views.timetable, name='timetable'),
    path('trainers', views.trainers, name='trainers'),
    path('trainer/<int:trainer_id>/', views.trainer, name='trainer'),
    path('view/', views.view_classes, name='view_class'),
    path('add/', views.add_class, name='add_class'),
    path('edit/<int:class_id>/', views.edit_class, name='edit_class'),
    path('delete/<int:class_id>/', views.delete_class, name='delete_class'),
]
