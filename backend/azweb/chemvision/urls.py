from django.urls import path

from . import views

app_name = "chemvision"

urlpatterns = [
    path('/',views.user_register, name = 'register'),
    path('/lecture_1',views.Lecture_1, name = 'lecture_1'),
    path('/lecture_2',views.Lecture_2, name = 'lecture_2'),
    path('/lecture_3',views.Lecture_3, name = 'lecture_3'),
    path('/lecture_4',views.Lecture_4, name = 'lecture_4'),
    path('/lecture_5',views.Lecture_5, name = 'lecture_5'),
]