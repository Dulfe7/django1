from .models import UserDevice
from django.core.mail import send_mail


class UserDeviceMixin:
    def save_user_device_info(self, request):
        # Сохранить информацию об устройстве пользователя при каждом входе
        user_device = UserDevice(
            user=request.user,
            ip_address=self.get_client_ip(request),
            device_name=request.META.get('HTTP_USER_AGENT')
        )
        user_device.save()

    def get_client_ip(self, request):
        # Получить IP-адрес пользователя из запроса
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def check_device_mismatch(self, request):
        user_devices = UserDevice.objects.filter(user=request.user).order_by('-login_time')
        if len(user_devices) >= 2:
            latest_device = user_devices[0]
            previous_device = user_devices[1]
            if latest_device.ip_address != previous_device.ip_address or latest_device.device_name != previous_device.device_name:
                subject = 'Warning: Possible unauthorized login attempt'
                message = f'Hello {request.user.username},\n\nThere was a login attempt from a different location/device.\n\nIf this was not you, please secure your account.\n\nBest regards,\nYour Website Team'
                send_mail(subject, message, 'from@example.com', [request.user.email], fail_silently=False)
