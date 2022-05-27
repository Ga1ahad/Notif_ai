from django.urls import path
from auth.views import CreateUserView
from rest_framework.authtoken.views import ObtainAuthToken

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('token/', ObtainAuthToken.as_view(), name='token'),
]
