from django.urls import path

from . import views

app_name = "qviz_it"

urlpatterns = [
    path('/register_non_iitb',views.user_register_non_iitb, name = 'register_non_iitb'),
    path('/register_iitb',views.user_register, name = 'register'),
    path('/leaderboard',views.Leaderboard, name = 'leaderboard'),
]



