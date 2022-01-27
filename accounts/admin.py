from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.


class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'username', 'last_login', 'phone',
                    'is_active', 'is_staff', 'is_admin', 'is_superadmin', 'is_verified')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    Fieldset = ()


admin.site.register(Account)
