from django.urls import path
from .views import (
    FootballFieldListView,
    FootballFieldCreateView,
    FootballFieldRetrieveView,
    FootballFieldUpdateView,
    FootballFieldDestroyView, FieldImageCreateView
)

urlpatterns = [
    path('fields/', FootballFieldListView.as_view(), name='footballfield-list'),
    path('fields/create/', FootballFieldCreateView.as_view(), name='footballfield-create'),
    path('fields/<int:pk>/', FootballFieldRetrieveView.as_view(), name='footballfield-detail'),
    path('fields/<int:pk>/update/', FootballFieldUpdateView.as_view(), name='footballfield-update'),
    path('fields/<int:pk>/delete/', FootballFieldDestroyView.as_view(), name='footballfield-delete'),
    path('fields/<int:field_id>/images/', FieldImageCreateView.as_view(), name='field-image-create'),
]
