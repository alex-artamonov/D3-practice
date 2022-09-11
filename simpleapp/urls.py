from django.urls import path
from .views import ProductDetail, ProductsList

urlpatterns = [
    path('', ProductsList.as_view()),
    path("<int:pk>", ProductDetail.as_view()),
]