from rest_framework import serializers

from measurement.models import Sensor, Measurment


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['name','discription']


class MeasurmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measurment
        fields = ['id','temperature','date']
# TODO: опишите необходимые сериализаторы
