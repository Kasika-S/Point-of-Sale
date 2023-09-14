from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    recoveryToken = models.CharField(max_length=100)


class Purchase(models.Model):
    #TODO add category choices in day 9
    sku = models.CharField(max_length=255, primary_key=True)
    purchase_order = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=True)
    supplier = models.CharField(max_length=255)
    quantity = models.BigIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=1)
    total = models.DecimalField(max_digits=8, decimal_places=1)
    expire_date = models.DateField()


class Inventory(models.Model):
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    slug = models.SlugField(default='-')
    category = models.CharField(max_length=255)
    uom = models.CharField(max_length=255)
    reorder_point = models.BigIntegerField()
    total_purchases = models.DecimalField(max_digits=8,decimal_places=2)
    total_sales = models.DecimalField(max_digits=8,decimal_places=2)
    stock_available_main = models.BigIntegerField()
    stock_available_for_sale = models.BigIntegerField()
    stock_available_value = models.DecimalField(max_digits=5, decimal_places=2)
    a_s_value = models.DecimalField(max_digits=5, decimal_places=2)
    best_selling_product = models.CharField(max_length=255)

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

