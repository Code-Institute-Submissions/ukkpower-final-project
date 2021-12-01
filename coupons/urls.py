from django.urls import path
from . import views

urlpatterns = [
    path('view/', views.view_coupons, name='view_coupons'),
    path('add/', views.add_coupon, name='add_coupon'),
    path('edit/<int:coupon_id>/', views.edit_coupon, name='edit_coupon'),
    path('delete/<int:coupon_id>/', views.delete_coupon, name='delete_coupon'),
]
