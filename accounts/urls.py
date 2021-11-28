from django.urls import path
from .views import LoginView, SignupView, ImagesView, ImagesDetailView

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('signup/', SignupView.as_view()),
    path( 'images/', ImagesView.as_view()),
    path( 'images/<int:user_id>/', ImagesDetailView.as_view()),
]
