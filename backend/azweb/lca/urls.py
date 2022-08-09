from django.urls import path

from . import views

app_name = "lca"

urlpatterns = [
    path('/',views.user_register, name = 'register'),
]
