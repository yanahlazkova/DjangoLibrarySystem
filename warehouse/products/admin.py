from django.contrib import admin

from products.models import Product, TypeProduct, Storage


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type')

admin.site.register(Product, ProductAdmin)


class TypeProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'date_to', 'user_moderator')

admin.site.register(TypeProduct, TypeProductAdmin)


class StorageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'product')

admin.site.register(Storage, StorageAdmin)
