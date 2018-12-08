from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from accounts.models import CompleteUser

# Define an inline admin descriptor for CompleteUser model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = CompleteUser
    can_delete = False
    verbose_name_plural = 'CompleteUser'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)