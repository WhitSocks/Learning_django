from pstats import Stats
import statistics
from telnetlib import STATUS
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view,action
from rest_framework.decorators import  parser_classes
from rest_framework.parsers import JSONParser
from rest_framework import viewsets
from .models import Drone,Medication,DroneMedication,BatteryLog
from .serialize import DroneSerializer,MedicationSerializer,DroneMedicationSerializer,BatteryLogSerializer

class DroneModelViewSet(viewsets.ModelViewSet):
   queryset = Drone.objects.all()
   serializer_class = DroneSerializer


   





class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class DroneMedicationViewSet(viewsets.ModelViewSet):
    queryset = DroneMedication.objects.all()
    serializer_class = DroneMedicationSerializer

class BatteryLogViewSet(viewsets.ModelViewSet):
    queryset = BatteryLog.objects.all()
    serializer_class = BatteryLogSerializer

@api_view(['GET'])
@parser_classes([JSONParser])
def drones_with_low_battery(request):
    # Get all Drones with a battery_capacity below 25
    drones = Drone.objects.filter(battery_capacity=125)

    # Serialize the Drone instances
    serializer = DroneSerializer(drones, many=True)

    # Return a response with the serialized Drone instances
    return Response(serializer.data)



