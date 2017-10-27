from rest_framework import serializers
from .models import ConfiTCL


class ConfiTCLSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ConfiTCL
        fields = ('id','user', 'number_of_PCL', 'PCL_amount',)
