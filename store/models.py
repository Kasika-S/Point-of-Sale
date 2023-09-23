from django.db import models 
from django.utils import timezone
import uuid

# unique token
def generate_unique_token():
    return str(uuid.uuid4())

class User(models.Model):
    ADMIN = '1'
    WORKER = '2'
    ROLE_CHOICES = [
        (ADMIN, 'Admin'),
        (WORKER, 'Worker'),
    ]
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    recoveryToken = models.CharField(max_length=100,default=generate_unique_token, unique=True)
    user_role = models.CharField(max_length=255, choices=ROLE_CHOICES,default=WORKER)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username + " " + self.lastname


class Purchase(models.Model):
    UNIT_CHOICES = [
    ('pcs', 'Pieces'),
    ('kg', 'Kilograms'),
    ('m', 'Meters'),
    ('L', 'Liters'),
    ('lbs', 'Pounds'),
    ('gal', 'Gallons'),
    ]
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('beverage', 'Beverage'),
        ('household', 'Household'),
        ('other', 'Other'),
    ]
    sku = models.CharField(max_length=255, primary_key=True)
    purchase_order = models.CharField(max_length=100, unique=True)
    purchase_date = models.DateField(auto_now_add=True) # Default
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    slug = models.SlugField(default='-') # Default
    category = models.CharField(max_length=255,choices=CATEGORY_CHOICES,default='other')
    uom = models.CharField(max_length=255,choices=UNIT_CHOICES,default='kg')
    supplier = models.CharField(max_length=255)
    quantity = models.BigIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    discount = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=3)
    expire_date = models.DateField()

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        total_purchase = self.quantity
        stock_available_main = self.quantity
        stock_available_for_sale = self.quantity
        stock_available_value = self.quantity * self.unit_price

        # inventory
        inventory, created = Inventory.objects.get_or_create(sku=self)
        inventory.reorder_point = 5
        inventory.total_purchases = total_purchase
        inventory.stock_available_main += stock_available_main
        inventory.stock_available_for_sale += inventory.stock_available_main 
        inventory.stock_available_value = inventory.stock_available_main * self.unit_price


        if(inventory.total_sales > 1000):
            inventory.best_selling_product = True
        inventory.save()

    def __str__(self):
        return self.sku

class Inventory(models.Model):
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE, related_name='inventory')
    reorder_point = models.BigIntegerField(default=50)
    total_purchases = models.DecimalField(max_digits=10,decimal_places=3, default=0.0)
    total_sales = models.DecimalField(max_digits=10,decimal_places=3,default=0.0)
    stock_available_main = models.BigIntegerField(default=0)
    stock_available_for_sale = models.BigIntegerField(default=0)
    stock_available_value = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    best_selling_product = models.BooleanField(default=False)


class Reserved(models.Model):
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    quantity = models.BigIntegerField()

class Sale(models.Model):
    sale_order = models.CharField(max_length=100,primary_key=True)
    sale_date = models.DateField(auto_now_add=True)
    sku = models.ForeignKey(Purchase,on_delete=models.PROTECT,related_name='sales')
    quantity = models.BigIntegerField()
    discount = models.FloatField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=3)
    total_amount = models.DecimalField(max_digits=10, decimal_places=3)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        total_sale = self.quantity
        stock_available_main = self.quantity

        # Inventory
        inventory, created = Inventory.objects.get_or_create(sku=self.sku)
        inventory.total_sales += total_sale
        inventory.stock_available_main -= stock_available_main
        inventory.stock_available_for_sale = inventory.stock_available_main
        inventory.save()

    def __str__(self):
        return self.sale_order

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=10)
    discount = models.FloatField()
    creditlimit = models.DecimalField(max_digits=10, decimal_places=3)
    tinnumber = models.BigIntegerField()
    vrnnumber = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

