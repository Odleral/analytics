from django.urls import path
from .views import Exp_view

urlpatterns = [
    path('expenses/', Exp_view.as_view()),
    path('expenses/<int:pk>', Exp_view.as_view()),
    path('expenses/', Exp_view.as_view()),
]