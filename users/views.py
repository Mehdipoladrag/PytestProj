from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class TestView(TemplateView): 
    def get(self, request): 
        return render(request, 'users/signup.html')