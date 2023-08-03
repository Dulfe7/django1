from django.contrib import admin
from django.contrib.auth.models import User
from .models import UserDevice

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserDevice)