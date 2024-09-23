from django.urls import path
from .views import UserListView, CustomTokenObtainPairView, RegisterView

urlpatterns = [
    path('users/', UserListView.as_view(), name='user-list'),
    path('users/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', RegisterView.as_view(), name='register'),

]
