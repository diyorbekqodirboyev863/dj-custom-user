from django.contrib import admin
from .models import CustomUser, Rank
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class UserAdmin(BaseUserAdmin):
	model = CustomUser
	list_display = ('email', 'first_name', 'last_name', 'is_staff', 'is_active', 'rank')
	list_filter = ('is_staff', 'is_active', 'rank')
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Personal info', {'fields': ('first_name', 'last_name', 'rank')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions')}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'first_name', 'last_name', 'password1', 'password2', 'rank', 'is_active', 'is_staff'),
		}),
	)
	search_fields = ('email',)
	ordering = ('email',)

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Rank)
