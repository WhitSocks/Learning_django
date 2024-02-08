from django.urls import path
from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'drones', views.DroneModelViewSet)
router.register(r'medications', views.MedicationViewSet)

router.register(r'dronemedication', views.DroneMedicationViewSet)
router.register(r'batterylogs', views.BatteryLogViewSet)
urlpatterns = [
    path('Capture-Information/', include(router.urls)),
    path('batteryinfo/drones_with_low_battery/',views.drones_with_low_battery),
    path('batteryinfo/drones_battery/',views.drone_battery)
]

