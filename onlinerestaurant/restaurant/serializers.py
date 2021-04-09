from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *

class MealSerializer(serializers.ModelSerializer):

    class Meta:
        model = Meal
        fields= "__all__"

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'


class CategoryDetailSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)
    class Meta:
        model = Category
        fields = '__all__'


class MealToOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model= MealToOrder
        fields = ['id','meal','quantity']


class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    status = serializers.CharField(read_only=True)
    promo = serializers.SerializerMethodField()
    mto = MealToOrderSerializer(many=True)
    order_count = serializers.SerializerMethodField()






    class Meta:
        model = Order
        fields = ["id","total_sum","date_created","status","payment_type",
                  "worker","promocode","total","mto","order_count","promo"]

    def get_order_count(self, obj):
        obj.worker.order_count += 1
        obj.worker.save()



    def create(self, validated_data):
        mto_data = validated_data.pop('mto')
        order = Order.objects.create(**validated_data)
        for mto in mto_data:
            MealToOrder.objects.create(order=order, **mto)
        return order

    def get_total(self,obj):
        total_price = 0
        meal_to_order = obj.mto.all()
        for mto in meal_to_order:
            total_price += mto.quantity * mto.meal.price
        obj.total_sum = total_price
        obj.save()
        return 1

    def get_promo(self,obj):
        promocodes = Promocode.objects.all()
        for i in promocodes:
            print(i.code)
            if i.code == obj.promocode:
                obj.total_sum -= obj.total_sum // 100 * i.sale_amount
                obj.promocode.status = 'dead'
                obj.promocode.save()
                obj.save()
                print(4)



class WorkerSerializer(serializers.ModelSerializer):
    salary = serializers.SerializerMethodField()

    class Meta:
        model = Worker
        fields = '__all__'


    def get_salary(self,obj):
        salary = obj.salary
        if obj.order_count > 5:
            obj.salary += 100
            obj.save()





