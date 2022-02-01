from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . models import Account

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name',  'last_login', 'phone',
                    'is_active', 'is_staff', 'is_admin', 'is_superadmin', 'is_verified')


admin.site.register(Account, AccountAdmin)
