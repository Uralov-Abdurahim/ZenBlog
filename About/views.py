from django.shortcuts import render
from django.views.generic import ListView
from About.models import AboutModel, Team

class AboutView(ListView):
    model = AboutModel
    template_name = 'about.html'


    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['team'] = Team.objects.all()
        return data