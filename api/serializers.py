from rest_framework import serializers
from rest_framework.fields import CharField, IntegerField

from api.models import Message


class MessageSerializer(serializers.ModelSerializer):
    id = IntegerField(label='ID',  read_only=True)
    views = IntegerField(read_only=True)

    class Meta:
        model = Message
        fields = ['id', 'body', 'views']
