from django.urls import path
from Home.views import HomeListView
from Home import views

name= "Home"

urlpatterns = [
   path('', HomeListView.as_view(), name='home'),
   path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
   path('terms-of-use/', views.terms_of_use, name='terms_of_use'),

]