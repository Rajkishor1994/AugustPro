from django.contrib import admin

from .models import Shop,Category,Product,Media

class ShopAdmin(admin.ModelAdmin):
    list_display = ['id','shop_name','shop_location']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name','parent_cat','shop']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','category']

class MediaAdmin(admin.ModelAdmin):
    list_display = ['id','product','product_image']

admin.site.register(Shop,ShopAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Media,MediaAdmin)