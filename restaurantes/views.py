from rest_framework import viewsets
from .models import Restaurante, Prato
from .serializers import RestauranteSerializer, PratoSerializer

class RestauranteViewSet(viewsets.ModelViewSet):
    queryset = Restaurante.objects.all()
    serializer_class = RestauranteSerializer

class PratoViewSet(viewsets.ModelViewSet):
    queryset = Prato.objects.all()
    serializer_class = PratoSerializer
