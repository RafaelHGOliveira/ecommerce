from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from customer import models


class AddressInline(admin.StackedInline):
    model = models.Address
    extra = 1


class UserAdmin(BaseUserAdmin):
    inlines = (AddressInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'cpf', 'birth_date', 'phone_number', 'genre')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Informações pessoais', {'fields': ('email', 'first_name', 'last_name', 'cpf', 'birth_date', 'phone_number', 'genre')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )
    readonly_fields = ('last_login', 'date_joined', )


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Address)
