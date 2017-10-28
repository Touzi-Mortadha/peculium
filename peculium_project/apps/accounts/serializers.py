from rest_framework import serializers
from .models import UserProfile, Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'date_of_transaction','amount_sent','TCL_assigned','time_of_transaction')


class UserProfileSerializer(serializers.ModelSerializer):
    transactions= TransactionSerializer(many=True, required=False, partial=True)
    class Meta:
        model = UserProfile
        fields = ('id', 'transactions',)
