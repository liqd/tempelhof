from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ('last_login',)
    list_filter = UserAdmin.list_filter + ('last_login',)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
