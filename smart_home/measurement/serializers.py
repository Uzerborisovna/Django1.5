from rest_framework import serializers

# TODO: опишите необходимые сериализаторы

from .models import Sensor, Measurement


class MeasurementSerializer(serializers.ModelSerializer):
    """Сериализатор для измерений (используется в детальном выводе датчика)"""

    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at']


class SensorSerializer(serializers.ModelSerializer):
    """Сериализатор для списка датчиков (краткая информация)"""

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    """Сериализатор для детальной информации о датчике (с измерениями)"""
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']


class MeasurementCreateSerializer(serializers.ModelSerializer):
    """Сериализатор для создания нового измерения"""

    class Meta:
        model = Measurement
        fields = ['sensor', 'temperature']