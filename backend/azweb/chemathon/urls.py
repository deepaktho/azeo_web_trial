from django.urls import path

from . import views

app_name = "chemathon"

urlpatterns = [
    # path('',views.user_register_non_iitb, name = 'register_non_iitb'),
    path('/chemathon_questions',views.Chemathon_question, name = 'chemathon_questions'),
    path('/',views.user_register, name = 'register'),
]



