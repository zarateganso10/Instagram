from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from twistter.views import DashboardView, home, SignUp
from django.urls import reverse_lazy


urlpatterns = [
    path('', home, name='home'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('signin/', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(next_page= reverse_lazy('login')), name='logout'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]