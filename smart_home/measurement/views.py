# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from .models import Sensor, Measurement
from .serializers import (
    SensorSerializer,
    SensorDetailSerializer,
    MeasurementCreateSerializer
)


class SensorListCreateView(generics.ListCreateAPIView):
    """
    GET: Получить список всех датчиков
    POST: Создать новый датчик
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    """
    GET: Получить детальную информацию о датчике (с измерениями)
    PUT/PATCH: Изменить датчик (название и описание)
    """
    queryset = Sensor.objects.all()

    def get_serializer_class(self):
        # Для GET запроса используем детальный сериализатор
        if self.request.method == 'GET':
            return SensorDetailSerializer
        # Для PUT/PATCH используем обычный сериализатор
        return SensorSerializer


class MeasurementCreateView(generics.CreateAPIView):
    """
    POST: Добавить новое измерение
    """
    queryset = Measurement.objects.all()
    serializer_class = MeasurementCreateSerializer