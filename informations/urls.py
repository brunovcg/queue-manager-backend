from django.urls import path
from .views import InformationsView, InformationsDetailView

urlpatterns = [
    path('informations/', InformationsView.as_view()),
    path('informations/<int:message_id>/', InformationsDetailView.as_view()),
]
