from rest_framework.authentication import TokenAuthentication
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from api.models import Message
from api.serializers import MessageSerializer


class MessageList(ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    authentication_classes = [TokenAuthentication]


class MessageDetailView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'id'
    authentication_classes = [TokenAuthentication]

    def retrieve(self, request, *args, **kwargs):
        message = self.get_object()
        message.increment_views()
        serializer = self.get_serializer(message)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        message = self.get_object()
        serializer = self.get_serializer(message, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        message.reset_views()
        return Response(serializer.data)
