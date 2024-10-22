from django.urls import path

from .views import get_item, get_items

urlpatterns = [
    path("items/", get_items),
    path("items/<int:id>/", get_item),
]
