from django.contrib.auth.admin import UserAdmin, admin

from .models import User


@admin.register(User)
class UserAdminCustom(UserAdmin):
    readonly_fields = ('jwt_token',)
    fieldsets = UserAdmin.fieldsets + (
        ('Информация', {'fields': (
            'jwt_token',)}),
    )