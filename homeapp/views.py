from django.shortcuts import render
from rest_framework import mixins,generics
from .models import Product
from .serializer import ProductSerializer
# Create your views here.

 

class ProductListMixinGenerics(
                                mixins.ListModelMixin,
                                generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class ProductRetrieveMixinGenerics(
                                   mixins.RetrieveModelMixin,
                                   generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)


class ProductCreateMixinGenerics(
                                mixins.CreateModelMixin,
                                generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class ProductUpdateMixinsGenerics(
                                mixins.UpdateModelMixin,
                                mixins.RetrieveModelMixin,
                                generics.GenericAPIView):

    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    

class ProductDestroyMixinGenerics(mixins.DestroyModelMixin,
                                mixins.RetrieveModelMixin,
                                generics.GenericAPIView,):
                                    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,*kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        