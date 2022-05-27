from django.urls import path
from api.views import MessageList, MessageDetailView

urlpatterns = [
    path('messages', MessageList.as_view(), name='messages'),
    path('messages/<int:id>', MessageDetailView.as_view(), name='message'),
]
