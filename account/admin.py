from account.models import *
from django.urls import reverse
from django.contrib import admin
from django.utils.html import format_html

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email', 
        'name', 
        'phone_number', 
        'role', 
        'is_active', 
        'created_at', 
        'actions'
    )
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('email', 'name', 'phone_number')
    ordering = ('-created_at',)

    def actions(self, obj):
        change_url = reverse('admin:account_user_change', args=[obj.pk])
        delete_url = reverse('admin:account_user_delete', args=[obj.pk])
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            change_url,
            delete_url
        )
    actions.short_description = 'Actions'
