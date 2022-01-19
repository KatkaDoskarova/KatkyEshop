from django.urls import path
from Account import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
