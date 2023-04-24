from django.contrib import admin
from .models import Article, Category

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('user','created_at', 'update_at')
    search_fields = ('title', 'content', 'user__username', 'categories__name')
    list_display = ('title', 'public', 'user', 'created_at')
    list_filter = ('public', 'user__username', 'categories__name')
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        obj.save()

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

    
# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)