from django.urls import path
from .views import *

urlpatterns = [
    path('meals/',MealView.as_view()),
    path('category/',CategoryView.as_view()),
    path('category/<int:meal_id>/',CategoryDetailView.as_view()),
    path('order/',OrderView.as_view()),
    path('worker/',WorkerView.as_view()),
]