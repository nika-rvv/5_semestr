from django.urls import path
from rip import views

urlpatterns = [
    path('', views.index),
    path('create/', views.create),
    path('create_language/', views.create_language),
    path('edit/<int:id>/', views.edit),
    path('edit_devtool/<int:id>/', views.edit_devtool),
    path('delete/<int:id>/', views.delete),
    path('delete_devtool/<int:id>/', views.delete_devtool),
    ]
