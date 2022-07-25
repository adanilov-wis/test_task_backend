from rest_framework import serializers

from couriers.models import Courier


class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = '__all__'


class StartWorkingSerializer(serializers.ModelSerializer):
    current_location = serializers.ListField(min_length=2, max_length=2, required=True)

    def validate_current_location(self, value):
        try:
            map(float, value)
            return value
        except ValueError:
            raise serializers.ValidationError('Given location is incorrect')

    class Meta:
        model = Courier
        fields = ['id', 'current_location']
