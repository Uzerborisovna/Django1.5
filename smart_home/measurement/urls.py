from django.urls import path


    # TODO: зарегистрируйте необходимые маршруты
from .views import (
    SensorListCreateView,
    SensorRetrieveUpdateView,
    MeasurementCreateView
)

urlpatterns = [
    # Датчики
    path('sensors/', SensorListCreateView.as_view(), name='sensor-list-create'),
    path('sensors/<int:pk>/', SensorRetrieveUpdateView.as_view(), name='sensor-detail'),

    # Измерения
    path('measurements/', MeasurementCreateView.as_view(), name='measurement-create'),
]