from django.urls import path
from .views import *

urlpatterns = [
    path('expenses/', Exp_view.as_view()),
    path('expenses/<int:pk>/', expense_detail),
    path('expenses/<int:pk>/', Exp_view.as_view()),
    path('expenses/odr/', ODRView.as_view()),
]