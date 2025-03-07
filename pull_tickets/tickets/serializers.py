from rest_framework import serializers
from tickets.views import Ticket


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'topic', 'is_available']
