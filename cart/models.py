from django.db import models
from inventory.models  import Product



class Cart(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)

    products=models.ManyToManyField(Product)

    # python3 makemigrations cart
    # python3 manage.py migrate
    # python3 manage.py runserver

    customer_ID = models.IntegerField()
    list_of_items = models.IntegerField()
    quantity_of_items = models.CharField(max_length=6)
   

    def add_product(self, product):
        self.products.add(product)
        self.save()
        return self 
    
    def calculate_total(self):
        products= self.product.all()
        total=0
        for product in products:
            total+= product.price
            return total
        

    


        