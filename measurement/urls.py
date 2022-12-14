from django.urls import path

from measurement.views import SensorsView, SensorUpdate

urlpatterns = [
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorUpdate.as_view()),
    # TODO: зарегистрируйте необходимые маршруты
]
