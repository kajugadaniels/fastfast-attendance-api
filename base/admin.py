from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Employee, FoodMenu, Attendance

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'phone', 
        'gender', 
        'position', 
        'salary', 
        'finger_id', 
        'status', 
        'created_at',
        'action_links'
    )
    list_filter = ('gender', 'position', 'status', 'created_at')
    search_fields = ('name', 'phone', 'finger_id')
    ordering = ('-created_at',)

    def action_links(self, obj):
        change_url = reverse('admin:base_employee_change', args=[obj.pk])
        delete_url = reverse('admin:base_employee_delete', args=[obj.pk])
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            change_url,
            delete_url
        )
    action_links.short_description = 'Actions'

@admin.register(FoodMenu)
class FoodMenuAdmin(admin.ModelAdmin):
    list_display = (
        'name', 
        'price', 
        'created_at', 
        'updated_at',
        'action_links'
    )
    list_filter = ('created_at',)
    search_fields = ('name',)
    ordering = ('-created_at',)

    def action_links(self, obj):
        change_url = reverse('admin:base_foodmenu_change', args=[obj.pk])
        delete_url = reverse('admin:base_foodmenu_delete', args=[obj.pk])
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            change_url,
            delete_url
        )
    action_links.short_description = 'Actions'

@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = (
        'employee', 
        'food_menu', 
        'finger_id', 
        'attendance_date', 
        'time_in', 
        'attended',
        'action_links'
    )
    list_filter = ('attended', 'attendance_date')
    search_fields = ('employee__name', 'finger_id')
    ordering = ('-time_in',)

    def action_links(self, obj):
        change_url = reverse('admin:base_attendance_change', args=[obj.pk])
        delete_url = reverse('admin:base_attendance_delete', args=[obj.pk])
        return format_html(
            '<a href="{}">Edit</a> | <a href="{}">Delete</a>',
            change_url,
            delete_url
        )
    action_links.short_description = 'Actions'
