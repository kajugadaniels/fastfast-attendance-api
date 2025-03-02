from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'name',
        'phone_number',
        'role',
        'is_active',
        'created_at',
        'action_links'  # renamed from "actions"
    )
    list_filter = ('role', 'is_active', 'created_at')
    search_fields = ('email', 'name', 'phone_number')
    ordering = ('-created_at',)

    def action_links(self, obj):
        change_url = reverse('admin:account_user_change', args=[obj.pk])
        delete_url = reverse('admin:account_user_delete', args=[obj.pk])
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            change_url,
            delete_url
        )
    action_links.short_description = 'Actions'
