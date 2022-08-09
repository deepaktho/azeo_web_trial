from django.urls import path

from . import views

app_name = "cipher"

urlpatterns = [
    path('/',views.user_register, name = 'register'),
    path('/portal',views.Portal_user, name = 'portal_user'),
    path('/portal/instructions',views.Instructions, name = 'instructions'),
    path('/portal/home',views.Home, name = 'home'),
    path('/portal/instructions',views.Instructions, name = 'instructions'),
    path('/portal/leaderboard',views.Leaderboard, name = 'leaderboard'),
]
