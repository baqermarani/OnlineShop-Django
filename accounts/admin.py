from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserUpdateForm
from .models import User , otpCode


# Register your models here.
@admin.register(otpCode)
class otpCodeAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'code' , 'created_at']



class UserAdmin(BaseUserAdmin):
    form = UserUpdateForm
    add_form = UserCreationForm

    list_display = ('email', 'phone_number', 'is_admin',)
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name' ,'password')}),
        ('Permissions', {'fields': ('is_admin','is_active','is_superuser','last_login','groups','user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('email', 'phone_number', 'full_name', 'password1', 'password2')}),
    )
    search_fields = ('email','full_name')
    ordering = ('email',)
    filter_horizontal = ('groups','user_permissions')
    readonly_fields = ('last_login',)

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].widget.attrs['disabled'] = True
        return form


admin.site.register(User, UserAdmin) # Register the UserAdmin class