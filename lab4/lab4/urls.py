

from django.contrib import admin
from django.urls import path
from BMSTU import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.GetDogs, name = 'main'),
    path('dog/<str:name>/', views.GetDog, name = "dog_url")
]
