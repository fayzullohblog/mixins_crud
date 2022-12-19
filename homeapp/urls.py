from django.urls import path
from .views import ProductListMixinGenerics,ProductRetrieveMixinGenerics,ProductCreateMixinGenerics,ProductUpdateMixinsGenerics,ProductDestroyMixinGenerics

urlpatterns = [
    path('get/',ProductListMixinGenerics.as_view()),
    path('get/<int:pk>/',ProductRetrieveMixinGenerics.as_view()),

    path('post/',ProductCreateMixinGenerics.as_view()),
    path('put/<int:pk>/',ProductUpdateMixinsGenerics.as_view()),
    path('destroy/<int:pk>/',ProductDestroyMixinGenerics.as_view()),

]