from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'created_by', 'modified', 'modified_by')


class BaseModelTabularInline(admin.TabularInline):
    exclude = ('active', 'created', 'created_by', 'modified', 'modified_by')


class BaseModelStackedInline(admin.StackedInline):
    exclude = ('active', 'created', 'created_by', 'modified', 'modified_by')


@admin.register(User)
class UserAdmin(UserAdmin):
    pass
