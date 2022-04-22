from rest_framework import serializers
from .models import twitter_data


class twitter_dataSerializer(serializers.ModelSerializer):

    class Meta:
        model = twitter_data
        fields = '__all__'