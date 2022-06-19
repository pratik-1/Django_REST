from rest_framework import viewsets
from . import models
from . import serializers


class CustomerViewset(viewsets.ModelViewSet):
    queryset = models.Customers.objects.all()
    serializer_class = serializers.CustomerSerializer