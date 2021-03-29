from django.shortcuts import render
from rest_framework import views
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.


class MealView(views.APIView):
    def get(self,request,*args,**kwargs):
        meals = Meal.objects.all()

        serializer = MealSerializer(meals,many=True)
        return Response(serializer.data)


class CategoryView(views.APIView):
    def get(self, request, *args, **kwargs):
        meals = Category.objects.all()

        serializer = CategorySerializer(meals, many=True)
        return Response(serializer.data)


class CategoryDetailView(views.APIView):
    def get(self,request,*args,**kwargs):
        meals = Category.objects.get(id=kwargs['meal_id'])

        serializer = CategoryDetailSerializer(meals)
        return Response(serializer.data)



class OrderView(views.APIView):
    def get(self,request,*args,**kwargs):
        orders = Order.objects.all()

        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)


    def post(self,request,*args,**kwargs):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)



class WorkerView(views.APIView):
    def get(self,request,*args,**kwargs):
        workers = Worker.objects.all()

        serializer = WorkerSerializer(workers, many=True)
        return Response(serializer.data)



