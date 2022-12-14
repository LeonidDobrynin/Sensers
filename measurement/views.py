from rest_framework.generics import ListAPIView, RetrieveUpdateAPIView, RetrieveAPIView, ListCreateAPIView, \
    CreateAPIView

from measurement.models import Sensor, Measurment
from measurement.serializers import SensorSerializer


class SensorsView(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class SensorUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer

class MeasureCreate(CreateAPIView):
    queryset = Measurment.objects.all()



# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
