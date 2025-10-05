from django.urls import path
from Contact.views import ContactView

urlpatterns = [
    path('Contact/', ContactView.as_view(), name='contact'),
]