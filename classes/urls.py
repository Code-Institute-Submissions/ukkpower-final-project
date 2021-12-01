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
    path('trainer/view/', views.view_trainers, name='view_trainers'),
    path('trainer/add/', views.add_trainer, name='add_trainer'),
    path('trainer/edit/<int:trainer_id>/',
         views.edit_trainer, name='edit_trainer'),
    path('trainer/delete/<int:trainer_id>/', views.delete_trainer,
         name='delete_trainer'),
    path('timetable/view/', views.view_timetables, name='view_timetables'),
    path('timetable/add/', views.add_timetable, name='add_timetable'),
    path('timetable/edit/<int:timetable_id>/', views.edit_timetable,
         name='edit_timetable'),
    path('timetable/delete/<int:timetable_id>/', views.delete_timetable,
         name='delete_timetable'),
]
