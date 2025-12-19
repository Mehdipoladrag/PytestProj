from django.urls import path
from .views import TestView


app_name = 'users'

urlpatterns = [
    path('signup', TestView.as_view())
]