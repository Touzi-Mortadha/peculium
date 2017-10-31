from rest_framework import serializers
from .models import ConfiTCL, GetCurrency


class ConfiTCLSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ConfiTCL
        fields = ('id','user', 'number_of_PCL', 'PCL_amount',)



class GetCurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = GetCurrency
        fields =('Ethereum','Bitcoin','Euro')