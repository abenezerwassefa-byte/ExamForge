from django.contrib import admin
from .models import Profile, School


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'created_at', 'school', 'updated_at')
    list_filter = ('role', 'school')
    search_fields = ('user__username', 'user__email')


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = ('name', 'email', 'phone', 'address',
                    'is_active', 'created_at')

    list_filter = ('is_active',)

    search_fields = ('name', 'email', 'phone')
