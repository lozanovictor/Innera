from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserChangeForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username', 'email', 'password']

admin.site.register(CustomUser, CustomUserAdmin)
