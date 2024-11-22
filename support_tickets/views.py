from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import SupportTicket
from .serializers import SupportTicketSerializer


class SupportTicketViewSet(ModelViewSet):
    queryset = SupportTicket.objects.all()
    serializer_class = SupportTicketSerializer
