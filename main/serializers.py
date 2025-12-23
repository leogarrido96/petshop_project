from rest_framework import serializers
from .models import SiteConfiguration, ContactMessage


class SiteConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteConfiguration
        fields = '__all__'


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'message', 'created_at']
