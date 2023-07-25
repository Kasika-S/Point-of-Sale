from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    recoveryToken = models.CharField(max_length=100)



class Purchase(models.Model):
    sku = models.CharField(max_length=100, primary_key=True)
    purchase_order = models.CharField(max_length=100)
    purchase_date = models.DateField(auto_now_add=True)
    supplier = models.CharField(max_length=255)
    quantity = models.BigIntegerField()
    discount = models.FloatField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total = models.DecimalField(max_digits=5, decimal_places=2)

class inventory(models.Model):
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    item_name = models.CharField(max_length=255)
    item_description = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    uom = models.DecimalField(max_digits=5, decimal_places=2)
    reorder_point = models.BigIntegerField()
    total_purchases = models.DecimalField(max_digits=6,decimal_places=2)
    total_sales = models.DecimalField(max_digits=6,decimal_places=2)
    stock_available = models.BigIntegerField()
    a_s_value = models.DecimalField(max_digits=5, decimal_places=2)
    best_selling_product = models.CharField(max_length=255)


class Sale(models.Model):
    sale_order = models.CharField(max_length=100,primary_key=True)
    sale_date = models.DateField(auto_now_add=True)
    sku = models.ForeignKey(Purchase,on_delete=models.CASCADE)
    quantity = models.BigIntegerField()
    discount = models.FloatField()
    unit_price = models.DecimalField(max_digits=5, decimal_places=2)
    total_amount = models.DecimalField(max_digits=5, decimal_places=2)
    customer_id = models.ForeignKey(User,on_delete=models.CASCADE)
    #purchase_id = models.ForeignKey(Purchase,on_delete=models.CASCADE)

