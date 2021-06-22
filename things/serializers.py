from django.db.models import fields
from things.models import Thing
from rest_framework import serializers

class ThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thing
        fields = ('id', 'name', 'owner', 'description')