from django.contrib import admin


class BaseModelAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'created_by', 'modified', 'modified_by')
