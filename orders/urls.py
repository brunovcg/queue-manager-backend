from django.urls import path
from .views import OrdersView,OrdersBranchView

urlpatterns = [
    path('orders/', OrdersView.as_view()),
    path('orders/branch/<int:branch_id>/', OrdersBranchView.as_view())
]
