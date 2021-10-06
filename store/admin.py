from django.contrib import admin

from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Comment)
admin.site.register(ReturnManagement)
admin.site.register(WebsiteReport)
admin.site.register(FarmReport)
admin.site.register(OverallReport)
