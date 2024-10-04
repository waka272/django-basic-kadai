from django.urls import path
from crud import views

urlpatterns = [
    path('crud/detail/<int.pk>', views.ProductDetailView.as_view(), name="detail"),
]

