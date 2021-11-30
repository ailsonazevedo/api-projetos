from rest_framework import serializers
from ..models import Projetos

class ProjetosSerializers(serializers.ModelSerializer):
    class Meta:
        model = Projetos
        fields = "__all__"