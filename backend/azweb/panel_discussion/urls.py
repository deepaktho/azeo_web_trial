from django.urls import path

from . import views

app_name = "panel_discussion"

urlpatterns = [
    path('/',views.user_register, name = 'register'),
]