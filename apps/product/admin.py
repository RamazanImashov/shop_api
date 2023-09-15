from django.contrib import admin
from .models import Product, Category


# admin.site.register(Product)
admin.site.register(Category)



# class ProductAdmin(admin.ModelAdmin):
    # list_display = ['slug', 'title']
    # list_filter = ['title', 'price']
    # search_fields = ['title', 'description']

# admin.site.register(Product, ProductAdmin)

from apps.review.models import Comment

class CommentInline(admin.TabularInline):
    model = Comment

class ProductAdmin(admin.ModelAdmin):
    list_display = ['slug', 'title']
    list_filter = ['title', 'price']
    search_fields = ['title', 'description']
    inlines = [CommentInline]

admin.site.register(Product, ProductAdmin)
