from django.urls import path

from . import views

app_name = "IDP"

urlpatterns = [
    path('',views.user_register, name = 'register'),
]
