from django.urls import path
from . import views

urlpatterns = [
    path('gym_classes', views.gym_classes, name='gym_classes'),
    path('trainers', views.trainers, name='trainers'),
    path('trainer/<int:trainer_id>/', views.trainer, name='trainer'),
]
