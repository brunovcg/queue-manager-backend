from django.urls import path
from .views import KitchensView, KitchensDetailView, KitchensDetailOrdersView, KitchensDetailOrdersDetailView

urlpatterns = [
    path('kitchens/', KitchensView.as_view()),
    path('kitchens/<int:kitchen_id>/', KitchensDetailView.as_view()),
    path('kitchens/<int:kitchen_id>/orders/', KitchensDetailOrdersView.as_view()),
    path('kitchens/<int:kitchen_id>/orders/<int:order_id>', KitchensDetailOrdersDetailView.as_view())
]
