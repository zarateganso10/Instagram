from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.urls import reverse_lazy

from twistter.forms import UserModelForm


# Create your views here.

def home(request):
        return render(request, 'home.html')


class DashboardView(TemplateView):
        template_name = "twistter/dashboard.html"


class SignUp(generic.CreateView):
    form_class = UserModelForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
