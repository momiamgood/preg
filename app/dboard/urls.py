from django.urls import path, include
from django.views.generic import TemplateView
from .views import RegisterUserView
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('registration/', RegisterUserView.as_view(), name='registration')
]

