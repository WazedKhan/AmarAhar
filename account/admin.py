from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from account.models import Account

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class AccountInLine(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'accounts'


class UserAdmin(BaseUserAdmin):
    inlines = (AccountInLine,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)