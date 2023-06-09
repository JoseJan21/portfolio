from django.contrib import admin
from .models import Page
# Register your models here.

class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_filter = ('visible',)
    list_display = ('title', 'visible', 'created_at', 'updated_at')
    ordering = ('-created_at', '-updated_at')
admin.site.register(Page, PagesAdmin)

title = "Proyectos"
subtitle = "Panel de gestion"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle
