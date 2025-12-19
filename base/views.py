from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomePageView(TemplateView):
    def get(self, request): 
        return render(request, "base/homepage.html")