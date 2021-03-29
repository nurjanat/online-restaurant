from django.db import models

# Create your models here.

class Meal(models.Model):
    name = models.CharField(max_length=60)
    price = models.PositiveIntegerField()
    ingreads = models.CharField(max_length=89)
    portion =(
        ('0,7','0,7'),
        ('1','1')
    )
    category = models.ForeignKey('Category',on_delete=models.SET_NULL,null=True,related_name='meals')
    meal_type = models.CharField(max_length=8)


class Category(models.Model):
    name = models.CharField(max_length=90)


class Order(models.Model):
    total_sum = models.PositiveIntegerField(default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    statuses = (
        ('pending','pending'),
        ('finish','finish')
    )
    payment_types = (
        ('cash','cash'),
        ('card','card')
    )
    status = models.CharField(max_length=90,choices=statuses,default='pending')
    payment_type = models.CharField(max_length=90,choices=payment_types,default='cash')
    worker = models.ForeignKey('Worker',on_delete=models.SET_NULL,null=True,related_name='order')
    promocode = models.CharField(max_length=10,blank=True,null=True)


class Worker(models.Model):
    name = models.CharField(max_length=90)
    age = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()
    position = models.CharField(max_length=90)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    order_count = models.PositiveIntegerField()




class Promocode(models.Model):
    code = models.CharField(max_length=56)
    status = models.CharField(max_length=90)
    end_date = models.DateTimeField()
    sale_amount = models.PositiveIntegerField()




class MealToOrder(models.Model):
    order = models.ForeignKey('Order',on_delete=models.SET_NULL,null=True,related_name='mto')
    meal = models.ForeignKey('Meal',on_delete=models.SET_NULL,null=True,related_name='mealtoorder')
    quantity = models.PositiveIntegerField()