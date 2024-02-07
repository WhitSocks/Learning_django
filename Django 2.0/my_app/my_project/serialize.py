from rest_framework import serializers
from .models import Drone, Medication, BatteryLog,DroneMedication

class DroneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drone
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class BatteryLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BatteryLog
        fields = '__all__'

class DroneMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DroneMedication
        fields = '__all__'