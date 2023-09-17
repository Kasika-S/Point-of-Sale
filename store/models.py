from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    recoveryToken = models.CharField(max_length=100)


class Purchase(models.Model):
    sku = models.CharField(max_length=255, primary_key=True)
    purchase_order = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=True)
    supplier = models.CharField(max_length=255)
    quantity = models.BigIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=1)
    discount = models.DecimalField(max_digits=8, decimal_places=1, default=0.0)
    total = models.DecimalField(max_digits=8, decimal_places=1)
    expire_date = models.DateField()


class Inventory(models.Model):
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
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    category = models.CharField(max_length=255, choices=CATEGORY_CHOICES, default='food')
    uom = models.CharField(max_length=255,choices=UNIT_CHOICES,default='kg')
    reorder_point = models.BigIntegerField()
    total_purchases = models.DecimalField(max_digits=8,decimal_places=2)
    total_sales = models.DecimalField(max_digits=8,decimal_places=2,default=0.0)
    stock_available_main = models.BigIntegerField(default=0)
    stock_available_for_sale = models.BigIntegerField()
    stock_available_value = models.DecimalField(max_digits=8, decimal_places=2)
    best_selling_product = models.BooleanField(default=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.item_name)
        if self.stock_available_main == 0:
            self.stock_available_for_sale = 0

        super(Inventory, self).save(*args, **kwargs)
class Reserved(models.Model):
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    quantity = models.BigIntegerField()


class Sale(models.Model):
    sale_order = models.CharField(max_length=100,primary_key=True)
    sale_date = models.DateField(auto_now_add=True)
    sku = models.ForeignKey(Purchase,on_delete=models.PROTECT)
    quantity = models.BigIntegerField()
    discount = models.FloatField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber = models.CharField(max_length=10)
    discount = models.FloatField()
    creditlimit = models.DecimalField(max_digits=5, decimal_places=1)
    tinnumber = models.BigIntegerField()
    vrnnumber = models.BigIntegerField()

