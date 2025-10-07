from django.urls import path
from Home.views import HomeListView



urlpatterns = [
   path('', HomeListView.as_view(), name='home')
]