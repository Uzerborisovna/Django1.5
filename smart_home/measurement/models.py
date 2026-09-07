from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)


class Sensor(models.Model):
    """Модель датчика"""
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.CharField(max_length=200, blank=True, verbose_name="Описание")

    def __str__(self):
        return self.name


class Measurement(models.Model):
    """Модель измерения температуры"""
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.FloatField(verbose_name="Температура")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время измерения")

    def __str__(self):
        return f"{self.sensor.name} - {self.temperature}°C"