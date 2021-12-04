from django.urls import path
from .views import BranchesView, BranchesDetailView

urlpatterns = [
    path('branches/', BranchesView.as_view()),
    path('branches/<int:branch_id>/', BranchesDetailView.as_view())
]
