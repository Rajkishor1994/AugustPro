from rest_framework.serializers import ModelSerializer
from .models import Shop,Category,Product,Media

class ShopSerializer(ModelSerializer):
    class Meta:
        model = Shop
        fields = ['id','shop_name','shop_location']


class MediaSerializer(ModelSerializer):
    class Meta:
        model = Media
        fields = ['product_image']


class ProductSerializer(ModelSerializer):
    media = MediaSerializer(many=True)

    class Meta:
        model = Product
        fields = ['id','product_name','media']

class CategorySerializer(ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = Category
        fields = ['id','category_name','products']