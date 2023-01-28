from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import CustomUser

# Register your models here.


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email','username','last_name','ismi','manzil','age','is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None,{'fields' : ('ismi',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields' : ('ismi',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
