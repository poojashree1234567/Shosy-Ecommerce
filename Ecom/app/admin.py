from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import (
    Customer,
    Product,
    Cart,
    OrderPlaced,
    Banner,
    LiveSale
)


@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['id','image','alt_text']

@admin.register(LiveSale)
class LiveSaleModelAdmin(admin.ModelAdmin):
    list_display = ['id','discount_details','term_and_condition']
    
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id' ,'user' ,'name', 'locality' , 'city' , 'zipcode' , 'state' ]

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','brand','discount_price','description','category','product_image']

@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']



@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer_info','product','product_info','quantity','ordered_date','status']

    def customer_info(self, obj):
        # Generate the correct URL for the customer change page
        link = reverse("admin:app_customer_change", args=[obj.customer.pk])
        return format_html('<a href="{}">{}</a>', link, obj.customer.name)
    
    def product_info(self, obj):
        # Generate the correct URL for the product change page
        link = reverse("admin:app_product_change", args=[obj.product.pk])
        return format_html('<a href="{}">{}</a>', link, obj.product.title)