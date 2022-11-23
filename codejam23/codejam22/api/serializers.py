from rest_framework import serializers
from .models import listing, User


class listingSerializer(serializers.ModelSerializer):
    userSession = serializers.StringRelatedField()

    class Meta:
        model = listing
        fields = "__all__"


class userSerializer(serializers.ModelSerializer):
    request = serializers.ManyRelatedField

    class Meta:
        model = User
        fields = "__all__"
