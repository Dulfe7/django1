from django.contrib.auth.views import LoginView
from .mixins import UserDeviceMixin


class CustomLoginView(LoginView, UserDeviceMixin):
    def form_valid(self, form):
        self.save_user_device_info(self.request)
        return super().form_valid(form)
