from rest_framework import serializers
from .models import listing

class listingSerializer(serializers.ModelSerializer):

    class Meta:
        model = listing
        fields = '__all__'