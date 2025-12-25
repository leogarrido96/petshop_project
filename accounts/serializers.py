from rest_framework import serializers
from django.contrib.auth.models import User
from pets.serializers import PetSerializer
from addresses.serializers import AddressSerializer


class UserSerializer(serializers.ModelSerializer):
    pets = PetSerializer(many=True, read_only=True)
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            'id', 'username', 'first_name', 'last_name',
            'email', 'cpf', 'phone', 'profile_picture',
            'pets', 'addresses'
        ]
