from django.contrib import admin
from .models import Todo


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'created', 'completed', 'important')
    readonly_fields = ('created',)


admin.site.register(Todo, TodoAdmin)
