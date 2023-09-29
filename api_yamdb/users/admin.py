from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User
# Register your models here.

UserAdmin.fieldsets += (
    ('Extra Fields', {'fields': ('bio', 'role',)}),
)

admin.site.register(User, UserAdmin)
