from django.urls import path
from About.views import AboutView, Team

app_name = 'About'

urlpatterns = [
    path('About/', AboutView.as_view(), name='About'),
]