from django.db import models

# Create your models here.
class Delivery(models.Model):
    Recipient_name= models.CharField(max_length=20)
    Recipient_phone= models.BigIntegerField()
    Delivery_address= models.CharField(max_length=100)
    Delivery_date= models.DateTimeField()
    Delivery_status= models.CharField(max_length=34)