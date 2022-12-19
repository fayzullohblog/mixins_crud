from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    title=serializers.CharField()
    content=serializers.CharField()
    

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title=validated_data.get('title',instance.title)
        instance.content=validated_data.get('content',instance.content)
        instance.save()
        return instance
    

    
        