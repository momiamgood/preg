from django.views.generic import CreateView
from .models import AdvUser
from .forms import RegisterUserForm


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'registration/registration.html'
    form_class = RegisterUserForm

    from django.views.generic.base import TemplateView

    class RegisterDoneView(TemplateView):
        template_name = 'accounts/user_account.html'
