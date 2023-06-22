from django.contrib import admin

# Register your models here.
from .models import Delivery

class Delivery_admin(admin.ModelAdmin):
    list_display= ("Recipient_name","Recipient_phone","Delivery_address","Delivery_date","Delivery_status")

admin.site.register(Delivery,Delivery_admin)

