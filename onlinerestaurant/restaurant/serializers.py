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
    # promo = serializers.SerializerMethodField()
    mto = MealToOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ["id","total_sum","date_created","status","payment_type",
                  "worker","promocode","total","mto"]

    def get_total(self,obj):
        total_price = 0
        meal_to_order = obj.mto.all()
        for mto in meal_to_order:
            total_price += mto.quantity * mto.meal.price
        obj.total_sum = total_price
        obj.save()
        return 1

    # def get_promo(self,obj):
    #     promocodes = Promocode.objects.all()
    #     for i in promocodes:
    #         print(i.code)
    #         if i.code == obj.promocode:
    #             obj.total_sum -= obj.total_sum // 100 * i.sale_amount
    #             obj.save()
    #             print(4)

    def create(self, validated_data):
        mto_data = validated_data.pop('mto')
        order = Order.objects.create(**validated_data)
        for mto in mto_data:
            MealToOrder.objects.create(order=order, **mto)
        return Order


class WorkerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Worker
        fields = '__all__'


