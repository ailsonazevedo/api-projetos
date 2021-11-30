from rest_framework import viewsets
from .serializers import ProjetosSerializers
from ..models import Projetos

class ProjetosViewsets(viewsets.ModelViewSet):
    serializer_class = ProjetosSerializers
    queryset = Projetos.objects.all()