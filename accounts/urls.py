from django.urls import path
from .views import LoginView, SignupView, UserDetailView, ResetPasswordView, ChangePasswordView, UserView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path('users/', UserView.as_view()),
    path('users/<int:user_id>/', UserDetailView.as_view()),
    path('reset-password/', ResetPasswordView.as_view()),
    path('change-password/<int:user_id>/', ChangePasswordView.as_view()),
]
