from django.urls import path
from .views import HomeView, ContactView, AboutView, DashboardView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('contato/', ContactView.as_view(), name='contact'),
    path('sobre-nos/', AboutView.as_view(), name='about'),
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
]
