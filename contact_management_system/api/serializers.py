from rest_framework import serializers
from contacts.models import Contact
from django.contrib.auth.models import User


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user.pk
        return super().create(validated_data)    