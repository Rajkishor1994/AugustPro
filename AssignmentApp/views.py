from django.shortcuts import render
from rest_framework.response import Response
from .models import Shop,Category,Product,Media
from .serializers import CategorySerializer
from rest_framework import viewsets

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()